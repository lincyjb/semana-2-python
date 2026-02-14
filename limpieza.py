import pandas as pd


def cargar_datos(ruta):
    return pd.read_csv(ruta)


def limpiar_columnas(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


def eliminar_duplicados(df):
    return df.drop_duplicates()


def manejar_nulos(df):
    return df.fillna(method="ffill")
