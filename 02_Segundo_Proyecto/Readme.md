# Proyecto 02: Clasificador de Anomalías en Fresadoras CNC (Clean Architecture)

Solución de diagnóstico en tiempo real diseñada para predecir fallos críticos por sobreesfuerzo (OSF) y otras anomalías operativas en maquinaria CNC. El sistema destaca por su diseño modular, implementando Arquitectura Limpia (Clean Architecture) en el backend y comunicándose con un motor de Inteligencia Artificial independiente.

## 🏗️ Arquitectura de la Solución

El sistema está dividido en dos servicios principales completamente desacoplados:

**1. Microservicio de IA (`ml_service/`):**
* Desarrollado en **Python** utilizando **FastAPI**.
* Aloja el modelo predictivo de Machine Learning entrenado para detectar anomalías.
* Expone un endpoint REST que recibe un vector con la telemetría física de la fresadora y calcula la clase de fallo y si requiere mantenimiento.

**2. Backend API & Dashboard Web (`backend_api/`):**
* Desarrollado en **C# con .NET 8**.
* Estructurado rigurosamente bajo **Clean Architecture** (Domain, Application, Infrastructure, Api), garantizando la separación de responsabilidades.
* Implementa el patrón **CQRS** utilizando **MediatR** para el manejo de comandos y consultas, manteniendo los controladores extremadamente ligeros.
* Cuenta con un **Panel Web (Frontend)** embebido servido a través de archivos estáticos (`wwwroot/index.html`) usando HTML, Vanilla JS y Bootstrap. Esto proporciona una interfaz interactiva en tiempo real sin necesidad de levantar un framework frontend pesado o Swagger.

## ⚙️ Guía de Ejecución Local

Para levantar el sistema completo, es necesario ejecutar ambos entornos en paralelo:

**Paso 1: Iniciar el Microservicio de Python**

```bash
cd ml_service
# Activar entorno virtual (Recomendado)
venv\Scripts\activate # (En Windows)

# Instalar dependencias
pip install -r requirements.txt

# Correr el servidor Uvicorn
uvicorn main:app --reload
# (El microservicio de IA correrá en [http://127.0.0.1:8000](http://127.0.0.1:8000))
Paso 2: Iniciar la API en C# y el Panel de Control

Bash
cd backend_api/ClasificadorAnomalias.Api
# Compilar y ejecutar la solución .NET
dotnet build
dotnet run
Una vez en ejecución, abre tu navegador y dirígete a https://localhost:7100/index.html para interactuar con la interfaz gráfica.

📊 Formato de Telemetría (Pruebas)
El modelo procesa 6 variables clave provenientes de los sensores y configuración de la fresadora. Puedes usar los siguientes valores de prueba en el formulario web:

Ejemplo 1: Operación Segura

Tipo de Calidad: L - Baja

Temp. Aire (K): 298.1

Temp. Proceso (K): 308.6

Velocidad Rotación (RPM): 1551

Torque (Nm): 42.8

Desgaste Herramienta (min): 0

Ejemplo 2: Alerta Crítica (Fallo por sobreesfuerzo - OSF)

Tipo de Calidad: L - Baja

Temp. Aire (K): 305.5

Temp. Proceso (K): 318.2

Velocidad Rotación (RPM): 1250

Torque (Nm): 75.8

Desgaste Herramienta (min): 2235
