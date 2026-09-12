using MediatR;
using Microsoft.AspNetCore.Mvc;
using ClasificadorAnomalias.Application.Commands;
using ClasificadorAnomalias.Domain.Entities;

namespace ClasificadorAnomalias.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class DiagnosticoController : ControllerBase
{
    private readonly IMediator _mediator;

    public DiagnosticoController(IMediator mediator)
    {
        _mediator = mediator;
    }

    [HttpPost]
    public async Task<IActionResult> EvaluarMaquina([FromBody] LecturaTelemetria telemetria)
    {
        var command = new EvaluarAnomaliaCommand(telemetria);
        var diagnostico = await _mediator.Send(command);
        return Ok(diagnostico);
    }
}