from src.simulacion import generar_datos_crudos
import os

# Crear carpeta raw si no existe
os.makedirs("data/raw", exist_ok=True)

df = generar_datos_crudos()

df.to_csv("data/raw/datos_red_crudos.csv", index=False)

print("✔ Datos crudos generados en data/raw/datos_red_crudos.csv")
