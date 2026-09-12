using System;
using System.Collections.Generic;
using System.Text;

namespace ClasificadorAnomalias.Domain.Entities
{
     public class LecturaTelemetria
    {
        public string TipoCalidad { get; set; } = string.Empty;
        public double TemperaturaAire { get; set; }
        public double TemperaturaProceso { get; set; }
        public int VelocidadRotacion { get; set; }
        public double Torque { get; set; }
        public int DesgasteHerramienta { get; set; }
    }
}
