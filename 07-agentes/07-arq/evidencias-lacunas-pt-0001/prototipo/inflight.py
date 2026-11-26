import subprocess, time, os, signal, sys, threading, http.client
drain, shutdown, port = sys.argv[1], sys.argv[2], sys.argv[3]
env = dict(os.environ, SPIKE_MODE="block", SPIKE_DRAIN_MS=drain, SPIKE_SHUTDOWN_S=shutdown, ASPNETCORE_ENVIRONMENT="Production", ASPNETCORE_URLS=f"http://127.0.0.1:{port}", DOTNET_ROOT=os.environ.get("DOTNET_ROOT", ""), DOTNET_NOLOGO="1")
p = subprocess.Popen(["dotnet", "pub/SpikeApi.dll"], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(2.5)
def slow():
    try:
        c=http.client.HTTPConnection("127.0.0.1",int(port),timeout=40); c.request("GET","/slow"); r=c.getresponse(); r.read()
    except Exception as e: pass
th=threading.Thread(target=slow); th.start(); time.sleep(0.5)
t=time.time(); os.kill(p.pid, signal.SIGTERM); p.wait()
print(f"drain={drain}ms shutdownTimeout={shutdown}s with 1 in-flight 30s request: exit after {time.time()-t:.2f}s code={p.returncode}")
