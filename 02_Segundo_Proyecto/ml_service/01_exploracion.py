import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import pickle

df = pd.read_csv('data/ai4i2020.csv')


# 1. Transformar texto a números (Ordinal Encoding)
mapeo_calidad = {'L': 0, 'M': 1, 'H': 2}
df['Type_Encoded'] = df['Type'].map(mapeo_calidad)

# 2. Consolidar los 5 fallos en una sola columna Target (Multiclase)
# 0: Normal, 1: TWF, 2: HDF, 3: PWF, 4: OSF, 5: RNF
condiciones = [
    (df['TWF'] == 1),
    (df['HDF'] == 1),
    (df['PWF'] == 1),
    (df['OSF'] == 1),
    (df['RNF'] == 1)
]
valores_clase = [1, 2, 3, 4, 5]

# Aplicar las condiciones y asignar 0 si ninguna se cumple
df['Target'] = np.select(condiciones, valores_clase, default=0)

# Mostrar cómo quedó la distribución de la nueva columna Target
print("=== DISTRIBUCIÓN DE LA COLUMNA TARGET ===")
print("0: Normal | 1: TWF | 2: HDF | 3: PWF | 4: OSF | 5: RNF")
print(df['Target'].value_counts())

# Guardar el dataset procesado para el entrenamiento
""" df.to_csv('data/dataset_procesado.csv', index=False)
print("\nDataset procesado guardado con éxito en 'data/dataset_procesado.csv'") """


# 2. Seleccionar las variables predictoras (X) y la etiqueta objetivo (y)
# Se excluyen identificadores y las columnas binarias originales de fallos
X = df[['Type_Encoded', 'Air temperature [K]', 'Process temperature [K]', 
        'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']]
y = df['Target']

# 3. Dividir los datos (80% entrenamiento, 20% prueba)
# stratify=y asegura que la misma proporción de fallos raros vaya a ambas particiones
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4 Aplicar SMOTE exclusivamente al conjunto de entrenamiento
print("Generando datos sintéticos con SMOTE...")
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# 5. Entrenar el modelo con los datos balanceados
print("Entrenando el clasificador RandomForest sobre los datos balanceados...")
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train_smote, y_train_smote)

# 6. Evaluar el rendimiento en los datos de prueba originales y reales
print("\n=== REPORTE DE CLASIFICACIÓN CON SMOTE ===")
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=0))

# 7. Serializar y guardar el nuevo modelo robusto
with open('modelo_anomalias.pkl', 'wb') as f:
    pickle.dump(modelo, f)
print("\nModelo mejorado guardado exitosamente como 'modelo_anomalias.pkl'")
