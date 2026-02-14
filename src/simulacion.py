import pandas as pd
import numpy as np

def generar_datos_crudos(n=100, seed=42):
    """
    Genera datos sintéticos de generación térmica y renovable
    para simular despacho energético.
    """

    np.random.seed(seed)

    df = pd.DataFrame({
        'fecha': pd.date_range(start='2024-01-01', periods=n),
        'generacion_termica_gwh': np.random.uniform(30, 50, n),
        'generacion_renovable_gwh': np.random.uniform(80, 120, n)
    })

    # Introducir errores intencionales
    df.iloc[0, 1] = np.nan
    df.iloc[5, 2] = -99.9

    return df
