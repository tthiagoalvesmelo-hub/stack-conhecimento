# Validação independente do ARQ para o G3 (TASK-0007). Somente leitura; não instala nada.
# Uso: /workspace/venv-oas/bin/python validar-g3-openapi.py <openapi.yaml>
import sys, json, re, yaml
from yaml.constructor import ConstructorError
from openapi_spec_validator import validate
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

path = sys.argv[1]
fails = []
def check(cond, msg):
    print(("OK    " if cond else "FALHA ") + msg)
    if not cond: fails.append(msg)

class StrictLoader(yaml.SafeLoader): pass
def no_dups(loader, node, deep=False):
    seen = set()
    for k, _ in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in seen: raise ConstructorError(None, None, f"chave duplicada: {key}", k.start_mark)
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep)
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, no_dups)

text = open(path, encoding="utf-8").read()
spec = yaml.load(text, Loader=StrictLoader)
check(True, "YAML parse estrito (sem chaves duplicadas)")
validate(spec)
check(True, f"openapi-spec-validator: OpenAPI {spec['openapi']} válido; info.version={spec['info']['version']}")
check(spec['openapi'].startswith('3.1'), "openapi 3.1.x")
check(spec['info']['version'] == '1.0.0', "info.version 1.0.0")
check(list(spec['paths'].keys()) == ['/health'], "somente o caminho /health")
ops = [k for k in spec['paths']['/health'] if k in ('get','put','post','delete','options','head','patch','trace')]
check(ops == ['get'], f"somente operação get no OpenAPI (achado: {ops})")
check(spec.get('security') == [], "security: [] (contrato interno, sem autenticação)")
check('securitySchemes' not in spec.get('components', {}), "sem securitySchemes")
check(not re.search(r'(?i)force', text.replace('FORCE_*','').replace('`FORCE_*`','')) or True, "(informativo) menções a force")
# gancho de teste fora do contrato: nenhum parâmetro/cabeçalho/operação de forçar erro
param_names = [p.get('name') for p in spec['components'].get('parameters', {}).values()]
check(param_names == ['X-Request-Id'], f"único parâmetro = X-Request-Id (achado: {param_names})")
check('Retry-After' not in json.dumps(spec['components']['headers']) and not any('Retry-After' in json.dumps(r.get('headers', {})) for r in spec['components']['responses'].values()), "nenhum cabeçalho Retry-After declarado")
hdrs = spec['components']['headers']
for forb in ('Server','X-Powered-By','Access-Control-Allow-Credentials','Access-Control-Allow-Headers','Access-Control-Expose-Headers'):
    check(forb not in hdrs and not any(forb in r.get('headers', {}) for r in spec['components']['responses'].values()), f"cabeçalho proibido/ausente não declarado: {forb}")
check(hdrs['CacheControl']['schema'].get('const') == 'no-store', "Cache-Control const no-store")
check(hdrs['XContentTypeOptions']['schema'].get('const') == 'nosniff', "X-Content-Type-Options const nosniff")
check(hdrs['Allow']['schema'].get('const') == 'GET, HEAD', "Allow const 'GET, HEAD'")
for r in ('Ok','Unavailable','MethodNotAllowed','InternalError'):
    h = spec['components']['responses'][r]['headers']
    for need in ('Cache-Control','X-Content-Type-Options','X-Request-Id','Access-Control-Allow-Origin'):
        check(need in h, f"resposta {r} declara {need}")
check('Allow' in spec['components']['responses']['MethodNotAllowed']['headers'], "405 declara Allow")
check(all('Allow' not in spec['components']['responses'][r]['headers'] for r in ('Ok','Unavailable','InternalError')), "Allow só no 405")
resp_get = spec['paths']['/health']['get']['responses']
check(sorted(resp_get.keys()) == ['200','405','500','503'], f"respostas do GET = 200/405/500/503 (achado {sorted(resp_get)})")
check(spec['components']['responses']['Ok']['content'].keys() == {'application/json; charset=utf-8'}, "200 em application/json; charset=utf-8")
check(spec['components']['responses']['MethodNotAllowed']['content'].keys() == {'application/problem+json'}, "405 em application/problem+json")
check(spec['components']['responses']['InternalError']['content'].keys() == {'application/problem+json'}, "500 em application/problem+json")
sch = spec['components']['schemas']
for n in ('HealthOk','HealthUnavailable','ProblemBase'):
    check(sch[n].get('additionalProperties') is False, f"{n}: additionalProperties false")
check(sch['HealthOk']['required'] == ['status','version','timestamp'] and sch['HealthUnavailable']['required'] == ['status','version','timestamp'], "required = status, version, timestamp (200 e 503)")
check(sch['HealthOk']['properties']['status']['const'] == 'ok' and sch['HealthUnavailable']['properties']['status']['const'] == 'unavailable', "status ok (200) / unavailable (503)")
check(sch['ProblemBase']['properties']['type']['const'] == 'about:blank', "RFC 9457 type about:blank")
check((sch['ProblemMethodNotAllowed']['properties']['status']['const'], sch['ProblemInternalError']['properties']['status']['const'], sch['ProblemNotFound']['properties']['status']['const']) == (405,500,404), "problem status 405/500/404")

# Exemplos e vetores contra os esquemas
res = Resource.from_contents({**spec, "$schema": "https://json-schema.org/draft/2020-12/schema"}, default_specification=DRAFT202012)
reg = Registry().with_resource("urn:oas", res)
def errs(n, ex, fmt=True):
    v = Draft202012Validator({"$ref": f"urn:oas#/components/schemas/{n}"}, registry=reg, format_checker=FormatChecker() if fmt else None)
    return list(v.iter_errors(ex))
for r, n in [('Ok','HealthOk'),('Unavailable','HealthUnavailable'),('MethodNotAllowed','ProblemMethodNotAllowed'),('InternalError','ProblemInternalError')]:
    for ct, c in spec['components']['responses'][r]['content'].items():
        for en, e in c['examples'].items():
            check(not errs(n, e['value']), f"exemplo {r}/{en} válido contra {n}")
good_ts = ["2026-11-26T15:30:00.123Z","2026-01-01T00:00:00.000Z","2026-12-31T23:59:59.999Z"]
bad_ts = ["2026-11-26T15:30:00Z","2026-11-26T15:30:00.12Z","2026-11-26T15:30:00.1234Z","2026-11-26T15:30:00.123+00:00","2026-11-26T15:30:00.123-03:00","2026-11-26 15:30:00.123Z","2026-13-26T15:30:00.123Z","2026-11-26T24:00:00.000Z","2026-11-26t15:30:00.123z"]
for t in good_ts: check(not errs('Timestamp', t), f"timestamp aceito: {t}")
for t in bad_ts: check(bool(errs('Timestamp', t)), f"timestamp rejeitado: {t}")
good_v = ["0.1.0","1.0.0","10.20.30","0.2.0-rc.1","1.0.0-alpha","1.0.0-alpha.1","1.0.0-0.3.7","1.0.0-x-y-z.-"]
bad_v = ["","1","1.0","01.0.0","1.01.0","1.0.01","1.0.0+build5","1.0.0-rc.1+b","1.0.0-","1.0.0-01","1.0.0-rc..1","1.0.0-rc.","v1.0.0","1.0.0 ","1.0.0-rc_1"]  # "1.0.0\n" omitido: em Python "$" aceita \n final (artefato do motor); em ECMAScript/Node é rejeitado (ver regex-g3.mjs)
for v in good_v: check(not errs('ServiceVersion', v), f"version aceita: {v!r}")
for v in bad_v: check(bool(errs('ServiceVersion', v)), f"version rejeitada: {v!r}")
# achado informativo: o padrão de timestamp aceita datas inexistentes (ex.: 31 de fevereiro)
inv = "2026-02-31T10:00:00.000Z"
print(f"INFO  timestamp com data inexistente {inv} aceito pelo padrão: {not errs('Timestamp', inv, fmt=False)} (format date-time via FormatChecker rejeita: {bool(errs('Timestamp', inv, fmt=True))})")
uuid_re = re.compile(spec['components']['headers']['XRequestIdResponse']['schema']['pattern'])
check(bool(uuid_re.fullmatch("123e4567-e89b-42d3-a456-426614174000")), "UUID canônico aceito")
check(not uuid_re.fullmatch("123E4567-E89B-42D3-A456-426614174000"), "UUID maiúsculo rejeitado (padrão exige minúsculo)")
check(not uuid_re.fullmatch("123e4567e89b42d3a456426614174000"), "UUID sem hífens rejeitado")
print("RESULTADO:", "OK" if not fails else f"{len(fails)} FALHA(S)")
sys.exit(1 if fails else 0)
