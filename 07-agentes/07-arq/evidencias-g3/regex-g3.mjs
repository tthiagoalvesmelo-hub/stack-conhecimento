import { readFileSync } from 'node:fs';
// extrai os padrões do YAML sem depender de lib: leitura por regex simples das linhas "pattern:"
const y = readFileSync('/workspace/stack-memoria/stack-conhecimento/02-tecnica/contratos-api/portal-api/openapi.yaml','utf8');
const pats = [...y.matchAll(/^\s*pattern: '(.*)'\s*$/gm)].map(m => m[1]);
console.log('padrões encontrados:', pats.length);
const [uuid, semver, ts] = [pats.find(p=>p.includes('[0-9a-f]{8}')), pats.find(p=>p.includes('(0|[1-9][0-9]*)\\.(0|[1-9]')), pats.find(p=>p.includes('T(['))];
const R = {uuid: new RegExp(uuid), semver: new RegExp(semver), ts: new RegExp(ts)};
const t = (n, s) => console.log(n.padEnd(7), JSON.stringify(s).padEnd(40), R[n].test(s));
t('semver','1.0.0'); t('semver','1.0.0\n'); t('semver','0.2.0-rc.1'); t('semver','1.0.0+b'); t('semver','01.0.0'); t('semver','1.0.0-01');
t('ts','2026-11-26T15:30:00.123Z'); t('ts','2026-11-26T15:30:00.123Z\n'); t('ts','2026-11-26T15:30:00Z'); t('ts','2026-11-26T15:30:00.123+00:00');
t('uuid','123e4567-e89b-42d3-a456-426614174000'); t('uuid','123E4567-E89B-42D3-A456-426614174000'); t('uuid','123e4567-e89b-42d3-a456-426614174000\n');
// Timestamp gerado pelo próprio Node: toISOString() atende ao padrão?
let ok = 0; for (let i=0;i<100000;i++){ const d=new Date(Date.now()+i*997331); if (R.ts.test(d.toISOString())) ok++; }
console.log('toISOString() atende ao padrão em', ok, 'de 100000 amostras');
console.log('crypto.randomUUID() atende ao padrão de X-Request-Id:', Array.from({length:1000},()=>R.uuid.test(crypto.randomUUID())).every(Boolean));
console.log('Date(2026-02-31) é inválida?', Number.isNaN(new Date('2026-02-31T10:00:00.000Z').getTime()));
