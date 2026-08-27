from fastapi import FastAPI
from pydantic import BaseModel
import joblib

#Crea la instancia de la API

app = FastAPI(title="NASA Predictive Maintenance API")
modelo = joblib.load('modelo_nasa.pkl')

class TelemetriaMotor(BaseModel):
    sensores: list[float]
    
#El Controlador (El Endpoint)
@app.post("/predecir")

#Crea una función asíncrona o síncrona
def predecir_fallo(datos: TelemetriaMotor):
    entrada = [datos.sensores]
    prediccion = modelo.predict(entrada)
    # devuelves el diccionario usando int()
    return {"alerta_fallo": int(prediccion[0])}
