using System;
using System.Collections.Generic;
using System.Text;

namespace ClasificadorAnomalias.Domain.Entities
{
    public class Diagnostico
    {
        public int CodigoClase { get; set; }
        public string DiagnosticoModelo { get; set; } = string.Empty;
        public bool RequiereMantenimiento { get; set; }
    }
}
