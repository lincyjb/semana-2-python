from limpieza import cargar_datos, limpiar_columnas, eliminar_duplicados, manejar_nulos

RUTA_ENTRADA = "data/Inflacion_y_meta.csv"
RUTA_SALIDA = "data/inflacion_limpia.csv"


def main():
    df = cargar_datos(RUTA_ENTRADA)
    df = limpiar_columnas(df)
    df = eliminar_duplicados(df)
    df = manejar_nulos(df)

    df.to_csv(RUTA_SALIDA, index=False)

    print("✅ Archivo limpio generado en: data/inflacion_limpia.csv")


if __name__ == "__main__":
    main()
