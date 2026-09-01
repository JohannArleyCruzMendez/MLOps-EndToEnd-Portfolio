using MantenimientoPredictivo.Web.Models; // Asegúrate de que este namespace coincida con el tuyo
using MantenimientoPredictivo.Web.Models.DTOs;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using System.Text;
using System.Text.Json;

namespace MantenimientoPredictivo.Web.Controllers
{
    public class HomeController : Controller
    {
        private readonly IHttpClientFactory _httpClientFactory;

        // Inyección de dependencias a través del constructor
        public HomeController(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Predecir(string datosEntrada)
        {
            // 1. Validar que no llegue vacío
            if (string.IsNullOrWhiteSpace(datosEntrada))
            {
                ViewBag.Error = "Por favor ingrese los datos de telemetría.";
                return View("Index");
            }

            try
            {
                // 2. Limpiar y convertir el texto a una lista de números (Float)
                // Usamos CultureInfo.InvariantCulture para que C# entienda que el punto (.) es el separador decimal, sin importar el idioma de tu Windows.
                var listaSensores = datosEntrada
                    .Split(',')
                    .Select(s => float.Parse(s.Trim(), System.Globalization.CultureInfo.InvariantCulture))
                    .ToList();

                // 3. Validación de Arquitectura: Nuestro modelo de Python exige exactamente 21 columnas
                if (listaSensores.Count != 21)
                {
                    ViewBag.Error = $"El modelo requiere exactamente 21 valores de sensores. Usted ingresó {listaSensores.Count}.";
                    return View("Index");
                }

                // 4. Instanciar el cliente y preparar el DTO
                var client = _httpClientFactory.CreateClient("FastApiClient");
                var datosMotor = new TelemetriaMotorDto { sensores = listaSensores };

                // 5. Serializar y enviar a Python (FastAPI)
                var jsonContent = new StringContent(JsonSerializer.Serialize(datosMotor), Encoding.UTF8, "application/json");
                var response = await client.PostAsync("/predecir", jsonContent);

                if (response.IsSuccessStatusCode)
                {
                    var responseString = await response.Content.ReadAsStringAsync();
                    var resultado = JsonSerializer.Deserialize<PrediccionFalloDto>(responseString);
                    ViewBag.AlertaFallo = resultado?.alerta_fallo;
                    ViewBag.DatosIngresados = datosEntrada; // Guardamos lo que ingresó el usuario para mantenerlo en pantalla si queremos
                }
                else
                {
                    ViewBag.Error = $"Error del microservicio AI. Código HTTP: {response.StatusCode}";
                }
            }
            catch (FormatException)
            {
                ViewBag.Error = "Error de formato. Asegúrese de ingresar solo números separados por comas.";
            }
            catch (Exception ex)
            {
                ViewBag.Error = $"Ocurrió un error inesperado: {ex.Message}";
            }

            return View("Index");
        }


    }
}