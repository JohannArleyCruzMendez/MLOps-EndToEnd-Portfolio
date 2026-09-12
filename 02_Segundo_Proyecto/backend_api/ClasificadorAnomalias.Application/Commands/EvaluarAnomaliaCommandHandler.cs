using ClasificadorAnomalias.Application.Interfaces;
using ClasificadorAnomalias.Domain.Entities;
using MediatR;
using System;
using System.Collections.Generic;
using System.Text;

namespace ClasificadorAnomalias.Application.Commands
{
    public class EvaluarAnomaliaCommandHandler : IRequestHandler<EvaluarAnomaliaCommand, Diagnostico>
    {

        private readonly IMachineLearningService _mlService;

        public EvaluarAnomaliaCommandHandler(IMachineLearningService mlService)
        {
            _mlService = mlService;
        }

        public async Task<Diagnostico> Handle(EvaluarAnomaliaCommand request, CancellationToken cancellationToken)
        {
            return await _mlService.EvaluarTelemetriaAsync(request.Telemetria);
        }
    }
}
