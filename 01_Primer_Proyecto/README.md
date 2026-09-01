# Proyecto 01: Sistema de Mantenimiento Predictivo (MLOps End-to-End)

Solución de Inteligencia Artificial diseñada para anticipar fallos inminentes en motores turbofán (utilizando el dataset de referencia de la NASA) a través de un ecosistema desacoplado que integra Machine Learning con desarrollo web empresarial.

## 🏗️ Arquitectura de la Solución

El sistema está dividido en dos microservicios independientes que se comunican mediante HTTP:

1. **Microservicio de IA (`ml_service/`):** 
   * Desarrollado en **Python** utilizando **FastAPI**.
   * Aloja un modelo predictivo basado en `RandomForest` (Scikit-Learn).
   * Expone un endpoint REST (`/predecir`) que recibe un vector de 21 parámetros de telemetría y calcula el riesgo de fallo.

2. **Backend & Frontend (`backend_api/`):**
   * Desarrollado en **C#** con **ASP.NET Core MVC**.
   * Utiliza `IHttpClientFactory` para consumir el microservicio de manera segura y eficiente mediante inyección de dependencias.
   * Cuenta con una interfaz web dinámica que permite ingresar telemetría de sensores y visualizar alertas críticas en tiempo real.

## ⚙️ Guía de Ejecución Local

Para levantar el sistema completo, es necesario ejecutar ambos entornos en paralelo:

### Paso 1: Iniciar el Microservicio de Python
```bash
cd ml_service
# Activar entorno virtual
venv\Scripts\activate  # (En Windows)
# Instalar dependencias y correr Uvicorn
pip install -r requirements.txt
uvicorn main:app --reload
(El microservicio correrá en http://127.0.0.1:8000)

Paso 2: Iniciar la Aplicación Web en C#
Bash
cd backend_api/MantenimientoPredictivo.Web
dotnet build
dotnet run
📊 Formato de Telemetría (Pruebas)
El modelo procesa un arreglo exacto de 21 variables numéricas provenientes de los sensores del motor.

Ejemplo Motor Sano:
0.002, -0.0003, 518.67, 642.15, 1591.82, 1403.14, 14.62, 21.61, 553.75, 2388.04, 9044.07, 1.3, 47.49, 522.28, 2388.07, 8131.49, 8.4318, 0.03, 392.0, 39.0, 23.42

Ejemplo Motor con Fallo Inminente:
0.0009, 0.0, 518.67, 644.21, 1605.44, 1432.52, 14.62, 21.61, 551.25, 2388.28, 9055.12, 1.3, 48.20, 519.53, 2388.32, 8110.93, 8.5227, 0.03, 397.0, 38.42, 22.9588
