import pandas as pd


def cargar_datos(ruta):
    """
    Carga el archivo CSV y devuelve un DataFrame
    """
    return pd.read_csv(ruta)


def limpiar_columnas(df):
    """
    Limpia nombres de columnas:
    - Quita espacios
    - Pasa a minúsculas
    - Reemplaza espacios por _
    """
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


def eliminar_duplicados(df):
    """
    Elimina filas duplicadas
    """
    return df.drop_duplicates()


def manejar_nulos(df):
    """
    Rellena valores nulos con el valor anterior (forward fill)
    Compatible con pandas nuevos
    """
    return df.ffill()
