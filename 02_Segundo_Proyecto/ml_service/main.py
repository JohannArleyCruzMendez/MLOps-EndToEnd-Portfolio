from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle
import pandas as pd

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="API de Diagnóstico de Anomalías Industriales",
    description="Microservicio de ML para clasificar fallos en fresadoras en tiempo real.",
    version="1.0.0"
)

# Cargar el modelo Random Forest entrenado al iniciar el servidor
try:
    with open('modelo_anomalias.pkl', 'rb') as f:
        modelo = pickle.load(f)
except FileNotFoundError:
    raise RuntimeError("No se encontró el archivo modelo_anomalias.pkl. Entrena el modelo primero.")

# Esquema estricto de Pydantic para validar la telemetría entrante
class Telemetria(BaseModel):
    tipo_calidad: str = Field(..., description="'L' (Baja), 'M' (Media), 'H' (Alta)")
    temperatura_aire: float = Field(..., gt=0, description="Temperatura del aire en Kelvin")
    temperatura_proceso: float = Field(..., gt=0, description="Temperatura del proceso en Kelvin")
    velocidad_rotacion: int = Field(..., gt=0, description="Velocidad en RPM")
    torque: float = Field(..., ge=0, description="Fuerza de torque en Nm")
    desgaste_herramienta: int = Field(..., ge=0, description="Tiempo de desgaste en minutos")

@app.post("/diagnosticar")
def diagnosticar_maquina(datos: Telemetria):
    # 1. Validar y transformar la variable categórica
    mapeo_calidad = {'L': 0, 'M': 1, 'H': 2}
    if datos.tipo_calidad not in mapeo_calidad:
        raise HTTPException(status_code=400, detail="El tipo_calidad debe ser 'L', 'M' o 'H'")
    
    tipo_codificado = mapeo_calidad[datos.tipo_calidad]

    # 2. Reconstruir el DataFrame exacto que espera el modelo
    df_entrada = pd.DataFrame([[
        tipo_codificado,
        datos.temperatura_aire,
        datos.temperatura_proceso,
        datos.velocidad_rotacion,
        datos.torque,
        datos.desgaste_herramienta
    ]], columns=[
        'Type_Encoded', 'Air temperature [K]', 'Process temperature [K]', 
        'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'
    ])

    # 3. Ejecutar inferencia multiclase
    prediccion = int(modelo.predict(df_entrada)[0])

    # 4. Mapear el resultado numérico a diagnóstico industrial
    diagnosticos = {
        0: "Estado Normal - Operación Segura",
        1: "Alerta Crítica: Fallo por desgaste de herramienta (TWF)",
        2: "Alerta Crítica: Fallo por disipación de calor (HDF)",
        3: "Alerta Crítica: Fallo de suministro de energía (PWF)",
        4: "Alerta Crítica: Fallo por sobreesfuerzo (OSF)",
        5: "Alerta Crítica: Fallo aleatorio inminente (RNF)"
    }

    return {
        "codigo_clase": prediccion,
        "diagnostico_modelo": diagnosticos[prediccion],
        "requiere_mantenimiento": prediccion != 0
    }