import subprocess, time, os, signal, socket, sys, http.client, json
mode, drain, shutdown = sys.argv[1], sys.argv[2], sys.argv[3]
port = sys.argv[4]
env = dict(os.environ, SPIKE_MODE=mode, SPIKE_DRAIN_MS=drain, SPIKE_SHUTDOWN_S=shutdown, ASPNETCORE_ENVIRONMENT="Production",
           ASPNETCORE_URLS=f"http://127.0.0.1:{port}", DOTNET_ROOT=os.environ.get("DOTNET_ROOT", ""), DOTNET_CLI_TELEMETRY_OPTOUT="1", DOTNET_NOLOGO="1")
d = "dotnet"
p = subprocess.Popen([d, "pub/SpikeApi.dll"], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd="pub")
time.sleep(2.5)
def probe():
    t=time.time()
    try:
        c = http.client.HTTPConnection("127.0.0.1", int(port), timeout=1)
        c.request("GET", "/health", headers={"Connection":"close"}); r = c.getresponse(); r.read(); c.close()
        return r.status
    except Exception as e:
        return "ERR:"+type(e).__name__
t_term = time.time()
os.kill(p.pid, signal.SIGTERM)
res=[]
while p.poll() is None and time.time()-t_term < 15:
    s = probe(); res.append((round(time.time()-t_term,2), s)); time.sleep(0.2)
t_exit = time.time()-t_term
p.wait()
counts={}
for _,s in res: counts[str(s)]=counts.get(str(s),0)+1
first503=[t for t,s in res if s==503][:1]; last503=[t for t,s in res if s==503][-1:]
firsterr=[t for t,s in res if str(s).startswith("ERR")][:1]
print(json.dumps(dict(mode=mode, drain_ms=drain, shutdown_s=shutdown, exit_code=p.returncode, exit_after_s=round(t_exit,2), counts=counts, first503_s=first503, last503_s=last503, first_refused_s=firsterr)))
