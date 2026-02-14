import pandas as pd
import numpy as np

def generar_datos_simulados(n=100):
    np.random.seed(42)
    
    datos = pd.DataFrame({
        "anio": np.random.choice(range(2020, 2031), n),
        "capacidad_renovable": np.random.normal(5000, 1000, n),
        "emisiones_co2": np.random.normal(200, 50, n)
    })
    
    return datos
