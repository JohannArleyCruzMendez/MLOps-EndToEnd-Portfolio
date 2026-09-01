namespace MantenimientoPredictivo.Web.Models.DTOs
{
    public class TelemetriaMotorDto
    {

        // Debe llamarse "sensores" o configurar [JsonPropertyName] para que coincida con el JSON de FastAPI
        public List<float> sensores { get; set; } = new List<float>();
    }

}

