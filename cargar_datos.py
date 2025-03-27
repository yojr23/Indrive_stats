import pandas as pd

def cargar_y_limpiar_csv(ruta_archivo):
    """
    Carga un archivo CSV y elimina las dos primeras columnas.

    Parámetros:
    ruta_archivo (str): Ruta del archivo CSV a cargar.

    Retorna:
    pd.DataFrame: DataFrame con las dos primeras columnas eliminadas.
    """
    # Cargar el archivo CSV
    data = pd.read_csv('data/'+ruta_archivo)
    
    # Eliminar las dos primeras columnas
    cleaned_data = data.drop(columns=data.columns[:2])
    
    return cleaned_data
