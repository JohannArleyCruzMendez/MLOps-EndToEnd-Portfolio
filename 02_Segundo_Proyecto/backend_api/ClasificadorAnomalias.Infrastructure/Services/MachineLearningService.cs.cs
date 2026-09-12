using ClasificadorAnomalias.Application.Interfaces;
using ClasificadorAnomalias.Domain.Entities;
using System;
using System.Collections.Generic;
using System.Net.Http.Json;
using System.Text;
using System.Text.Json;

namespace ClasificadorAnomalias.Infrastructure.Services
{
    public class MachineLearningService : IMachineLearningService
    {

        private readonly HttpClient _httpClient;

        public MachineLearningService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }



        public async Task<Diagnostico> EvaluarTelemetriaAsync(LecturaTelemetria telemetria)
        {
            // Mapeamos las propiedades al formato snake_case que exige Pydantic en FastAPI
            var payload = new
            {
                tipo_calidad = telemetria.TipoCalidad,
                temperatura_aire = telemetria.TemperaturaAire,
                temperatura_proceso = telemetria.TemperaturaProceso,
                velocidad_rotacion = telemetria.VelocidadRotacion,
                torque = telemetria.Torque,
                desgaste_herramienta = telemetria.DesgasteHerramienta
            };
            var response = await _httpClient.PostAsJsonAsync("http://127.0.0.1:8000/diagnosticar", payload);

            response.EnsureSuccessStatusCode();

            // Configuramos la deserialización para que entienda el snake_case de Python
            var options = new JsonSerializerOptions { PropertyNamingPolicy = JsonNamingPolicy.SnakeCaseLower };
            var resultado = await response.Content.ReadFromJsonAsync<Diagnostico>(options);

            return resultado ?? new Diagnostico();

        }



    }
}