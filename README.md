# 🚀 Portafolio de MLOps y Arquitectura de Software End-to-End

Bienvenido a mi repositorio principal de proyectos. Como Máster en Desarrollo de Software con conocimientos en Inteligencia Artificial, este espacio está dedicado a demostrar la integración de modelos de Machine Learning en arquitecturas de software robustas, cerrando la brecha entre la experimentación de datos y los sistemas en producción.

## 📂 Directorio de Proyectos

A continuación se detallan las implementaciones técnicas desarrolladas, diseñadas bajo patrones de arquitectura limpia y microservicios.

### [1. Sistema de Mantenimiento Predictivo (NASA Dataset)](./01_Primer_Proyecto)
*Estado: Completado* ✅

Solución de Inteligencia Artificial diseñada para anticipar fallos inminentes en motores turbofán mediante el análisis de telemetría de 21 sensores. El proyecto demuestra la separación de responsabilidades entre la carga computacional matemática y la interfaz de usuario.
* **AI Microservice (Backend):** Modelo de clasificación `RandomForest` encapsulado y servido a través de una API RESTful con Python y FastAPI.
* **Web App (Frontend/BFF):** Plataforma web desarrollada en C# con ASP.NET Core MVC que consume el microservicio mediante inyección de dependencias (`IHttpClientFactory`) para un procesamiento dinámico y seguro de la telemetría.
* ➡️ [Ver detalles, arquitectura y código fuente del proyecto](./01_Primer_Proyecto)

### [2. Clasificador de Anomalías en Fresadoras CNC (Clean Architecture)](./02_Segundo_Proyecto)
*Estado: Completado* ✅

Sistema de diagnóstico en tiempo real para identificar fallos críticos por sobreesfuerzo (OSF) y otras anomalías operativas en maquinaria CNC. Este proyecto destaca por su diseño modular implementando Arquitectura Limpia (Clean Architecture) y el patrón CQRS para una comunicación eficiente.
* **AI Microservice (ML Engine):** Modelo de Machine Learning en Python que evalúa parámetros físicos (temperatura, rotación, torque, desgaste de herramienta) para determinar si la máquina requiere mantenimiento inmediato.
* **Backend API (.NET 8):** API desarrollada bajo **Clean Architecture** utilizando **MediatR** para el enrutamiento de comandos y separación de responsabilidades. Actúa como orquestador, gestionando peticiones asíncronas hacia el motor de IA.
* **Dashboard de Monitoreo (Frontend):** Interfaz gráfica interactiva y ligera implementada en HTML, JavaScript y Bootstrap. Se sirve nativamente mediante archivos estáticos (`wwwroot`) desde la API de .NET, permitiendo la visualización de telemetría y alertas críticas en tiempo real sin requerir un servidor frontend independiente.
* ➡️ [Ver detalles, arquitectura y código fuente del proyecto](./02_Segundo_Proyecto)

*Proyectos adicionales en fase de desarrollo se listarán aquí próximamente...*

## 🛠️ Stack Tecnológico Principal

* **Ingeniería de Software:** C#, .NET 8, .NET Core, ASP.NET Core MVC, Clean Architecture, Patrones de Diseño (CQRS, MediatR), Entity Framework Core.
* **Inteligencia Artificial & Datos:** Python, Scikit-Learn, Pandas, Numpy.
* **Arquitectura & MLOps:** APIs REST (FastAPI), Arquitectura de Microservicios, Inyección de Dependencias, Integración de Sistemas.


