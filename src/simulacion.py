import pandas as pd
import numpy as np
import os

# Crear carpetas si no existen
os.makedirs('datos', exist_ok=True)
os.makedirs('resultados', exist_ok=True)

# Generar 100 días de datos de red con "ruido"
np.random.seed(42)
df = pd.DataFrame({
    'fecha': pd.date_range(start='2024-01-01', periods=100),
    'generacion_termica_gwh': np.random.uniform(30, 50, 100),
    'generacion_renovable_gwh': np.random.uniform(80, 120, 100)
})

# Meter errores a propósito para que el script de limpieza trabaje
df.iloc[0, 1] = np.nan 
df.iloc[5, 2] = -99.9

df.to_csv('datos/datos_red_crudos.csv', index=False)
print("✅ Datos crudos generados en datos/datos_red_crudos.csv")