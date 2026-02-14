import pandas as pd
import matplotlib.pyplot as plt
import os

# Rutas relativas
ruta_datos = os.path.join('datos', 'datos_red_crudos.csv')
ruta_grafico = os.path.join('resultados', 'grafico_emisiones.png')
ruta_tabla = os.path.join('resultados', 'tabla_resumen.csv')

def generar_resultados():
    # Crear carpeta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')

    if not os.path.exists(ruta_datos):
        print(f"Error: No se encuentra {ruta_datos}")
        return

    # Leer datos
    df = pd.read_csv(ruta_datos)
    
    # 1. Generar la Figura (Obligatorio)
    plt.figure(figsize=(10,5))
    plt.plot(df['generacion_renovable_gwh'], color='green', label='Renovable')
    plt.plot(df['generacion_termica_gwh'], color='red', label='Térmica')
    plt.title('Simulación de Despacho Eléctrico - Colombia')
    plt.legend()
    plt.savefig(ruta_grafico)
    print(f"✅ Gráfico guardado en {ruta_grafico}")

    # 2. Generar la Tabla (Obligatorio)
    resumen = df.describe()
    resumen.to_csv(ruta_tabla)
    print(f"✅ Tabla resumen guardada en {ruta_tabla}")

if __name__ == "__main__":
    generar_resultados()