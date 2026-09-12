using ClasificadorAnomalias.Application.Interfaces;
using ClasificadorAnomalias.Infrastructure.Services;
using ClasificadorAnomalias.Application.Commands;
using MediatR;

var builder = WebApplication.CreateBuilder(args);

// Configuración para usar Controladores en lugar de Minimal APIs
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// 1. Inyección de dependencias para la Infraestructura (Cliente HTTP)
builder.Services.AddHttpClient<IMachineLearningService, MachineLearningService>();

// 2. Registro de MediatR apuntando al Assembly de la capa Application
builder.Services.AddMediatR(cfg =>
    cfg.RegisterServicesFromAssembly(typeof(EvaluarAnomaliaCommand).Assembly));

var app = builder.Build();

// Configuración de la interfaz visual de Swagger para probar la API
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();




 // AGREGAR ESTA LÍNEA: Permite leer archivos desde la carpeta wwwroot
app.UseStaticFiles();


// Enrutamiento automático hacia la carpeta Controllers


app.MapControllers();

app.Run();
