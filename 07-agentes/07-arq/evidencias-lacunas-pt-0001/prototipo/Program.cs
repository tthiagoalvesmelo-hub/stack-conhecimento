using System.Diagnostics;
var builder = WebApplication.CreateBuilder(args);
if (Environment.GetEnvironmentVariable("SPIKE_FILTER") == "1") builder.Logging.AddFilter("Microsoft.AspNetCore", LogLevel.Warning);
var origin = "http://localhost:4200";
builder.Services.AddCors(o => o.AddPolicy("p", p => p.WithOrigins(origin).WithMethods("GET", "HEAD")));
var drainMs = int.Parse(Environment.GetEnvironmentVariable("SPIKE_DRAIN_MS") ?? "3000");
var mode = Environment.GetEnvironmentVariable("SPIKE_MODE") ?? "block";
var requireCors = Environment.GetEnvironmentVariable("SPIKE_REQUIRECORS") == "1";
var shutdownS = int.Parse(Environment.GetEnvironmentVariable("SPIKE_SHUTDOWN_S") ?? "8");
builder.Services.Configure<HostOptions>(o => o.ShutdownTimeout = TimeSpan.FromSeconds(shutdownS));
if (mode == "hosted") builder.Services.AddHostedService(sp => new DrainSvc(drainMs));
var app = builder.Build();
var stopping = false; DrainSvc.OnStop = () => stopping = true;
var life = app.Lifetime;
var log = app.Services.GetRequiredService<ILoggerFactory>().CreateLogger("SpikeApi.Health");
var t0 = Stopwatch.StartNew();
life.ApplicationStopping.Register(() =>
{
    stopping = true;
    Console.WriteLine($"[spike] ApplicationStopping handler start t={DateTime.UtcNow:HH:mm:ss.fff}");
    if (mode == "block") Thread.Sleep(drainMs);
    Console.WriteLine($"[spike] ApplicationStopping handler end   t={DateTime.UtcNow:HH:mm:ss.fff}");
});
life.ApplicationStopped.Register(() => Console.WriteLine($"[spike] ApplicationStopped t={DateTime.UtcNow:HH:mm:ss.fff}"));
app.UseRouting();
if (!requireCors) app.UseCors("p");
var ep = app.MapGet("/health", (HttpContext c) =>
{
    log.LogDebug("health requested");
    if (stopping) return Results.Json(new { status = "unavailable" }, statusCode: 503);
    return Results.Json(new { status = "ok" });
});
if (requireCors) { ep.RequireCors("p"); app.UseCors("p"); }
app.MapGet("/slow", async (CancellationToken ct) => { await Task.Delay(30000); return Results.Ok("slow"); });
app.MapMethods("/health", new[] { "HEAD" }, () => Results.Ok());
if (Environment.GetEnvironmentVariable("SPIKE_LIST") == "1") {
  foreach (var e in ((Microsoft.AspNetCore.Routing.IEndpointRouteBuilder)app).DataSources.SelectMany(d => d.Endpoints)) {
    var re = e as Microsoft.AspNetCore.Routing.RouteEndpoint;
    var m = e.Metadata.GetMetadata<Microsoft.AspNetCore.Routing.HttpMethodMetadata>();
    Console.WriteLine($"[endpoint] {re?.RoutePattern.RawText} methods={string.Join(",", m?.HttpMethods ?? new List<string>())} acceptCorsPreflight={m?.AcceptCorsPreflight}");
  }
  return;
}
app.Run();

class DrainSvc : IHostedService {
  public static Action? OnStop; readonly int _ms; public DrainSvc(int ms) { _ms = ms; }
  public Task StartAsync(CancellationToken ct) => Task.CompletedTask;
  public async Task StopAsync(CancellationToken ct) { Console.WriteLine($"[spike] hosted StopAsync start t={DateTime.UtcNow:HH:mm:ss.fff}"); OnStop?.Invoke(); try { await Task.Delay(_ms, ct); } catch (OperationCanceledException) {} Console.WriteLine($"[spike] hosted StopAsync end t={DateTime.UtcNow:HH:mm:ss.fff}"); }
}
