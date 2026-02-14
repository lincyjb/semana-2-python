import pandas as pd
import matplotlib.pyplot as plt

RUTA = "data/inflacion_limpia.csv"


def main():
    # Cargar datos
    df = pd.read_csv(RUTA)

    print("\n===== PRIMERAS FILAS =====")
    print(df.head())

    print("\n===== INFO =====")
    print(df.info())

    print("\n===== ESTADÍSTICAS =====")
    print(df.describe())

    print("\n===== VALORES NULOS =====")
    print(df.isnull().sum())

    # Si existe columna fecha, convertir
    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
        df = df.sort_values("fecha")

    # Graficar inflación si existe
    if "inflacion" in df.columns:
        plt.figure()
        plt.plot(df["inflacion"])
        plt.title("Serie de Inflación")
        plt.xlabel("Observaciones")
        plt.ylabel("Inflación")
        plt.show()

    print("\n✅ EDA terminado")


if __name__ == "__main__":
    main()
import pandas as pd

df = pd.read_csv("data/inflacion_limpia.csv")

# Convertir a numérico
cols_num = [
    "inflación_total",
    "límite_inferior_meta_inflación",
    "meta_de_inflación",
    "límite_superior_meta_inflación"
]

for c in cols_num:
    df[c] = pd.to_numeric(df[c], errors="coerce")
print(df.describe())
import matplotlib.pyplot as plt

df["inflación_total"].plot()
plt.title("Inflación total en el tiempo")
plt.show()
