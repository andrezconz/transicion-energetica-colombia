from src.simulacion import generar_datos_simulados

import os

# Crear carpeta si no existe
os.makedirs("data/raw", exist_ok=True)

datos = generar_datos_simulados(200)
datos.to_csv("data/raw/datos_simulados.csv", index=False)

print("Datos simulados guardados en data/raw/")
