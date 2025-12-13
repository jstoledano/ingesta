var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.MapGet("/", () => "Ingesta API running");

app.Run();
