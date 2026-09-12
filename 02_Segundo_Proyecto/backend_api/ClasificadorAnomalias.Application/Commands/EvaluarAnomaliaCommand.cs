using ClasificadorAnomalias.Domain.Entities;
using MediatR;
using System;
using System.Collections.Generic;
using System.Text;

namespace ClasificadorAnomalias.Application.Commands
{
     public class EvaluarAnomaliaCommand : IRequest<Diagnostico>
    {
        public LecturaTelemetria Telemetria { get; set; }

        public EvaluarAnomaliaCommand(LecturaTelemetria telemetria)
        {
            Telemetria = telemetria;
        }
    }
}
