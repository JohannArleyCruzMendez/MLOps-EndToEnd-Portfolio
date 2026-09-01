import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import classification_report
import joblib 

# 1. Definimos las primeras 5 columnas con nombres limpios

columnas_base = ["engine_id", "time_cycle", "op_setting_1", "op_setting_2", "op_setting_3"]

# 2. Generamos los 21 sensores (del 1 al 21). El range(1, 22) llega hasta el 21.
columnas_sensores = [f"sensor_{i}" for i in range(1, 22)]

# 3. Concatenamos ambas listas (en Python, sumar dos listas las une)
todas_las_columnas = columnas_base + columnas_sensores

# 4. Leemos el archivo. El parámetro 'names' hace el trabajo sucio por nosotros.
df = pd.read_csv("data/train_FD001.txt", sep=r"\s+", names=todas_las_columnas)

print("--- PRIMERAS 5 FILAS ---")
print(df.head())

print("\n--- INFORMACIÓN DEL DATASET ---")
print(df.info())

print("\n--- ESTADÍSTICAS BÁSICAS ---")
print(df.describe())

print("\n--- VALORES NULOS POR COLUMNA ---")
print(df.isnull().sum())

df = df.drop(columns=["op_setting_3", "sensor_18","sensor_19"])

df.shape

ciclos_maximos = df.groupby('engine_id')['time_cycle'].max().reset_index()
ciclos_maximos.columns = ['engine_id', 'max_cycle']
df = pd.merge(df, ciclos_maximos, how='left', on='engine_id')
df['RUL'] = df['max_cycle'] - df['time_cycle']
df['label'] = (df['RUL'] <= 30).astype(int)

df[['engine_id', 'time_cycle', 'max_cycle', 'RUL', 'label']].head(10)

df[df['engine_id'] == 1].tail(10)

x = df.drop(['engine_id','time_cycle','max_cycle','RUL','label'], axis=1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print( "Datos de entrenamiento X" ,X_train.shape)
print( "Datos de entrenamiento y" ,y_train.shape)

modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)
print(classification_report(y_test, predicciones))

# persistencia del modelo Para que tu backend en C# pueda consumirlo,
# primero necesitamos que este modelo de Python sobreviva en el disco duro. 
# En C# haríamos esto serializando un objeto; en Machine Learning de Python, lo llamamos hacer un "Pickle".


joblib.dump(modelo, 'modelo_nasa.pkl')



    
    
    

