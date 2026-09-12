using ClasificadorAnomalias.Domain.Entities;
using System;
using System.Collections.Generic;
using System.Text;

namespace ClasificadorAnomalias.Application.Interfaces
{
     public interface IMachineLearningService
    {
        Task<Diagnostico> EvaluarTelemetriaAsync(LecturaTelemetria telemetria);
    }
}
