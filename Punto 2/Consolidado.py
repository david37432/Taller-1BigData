import pandas as pd
import os

# Cambiar cwd a la carpeta donde está el script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Directorio de trabajo:", os.getcwd())
from IPython.display import display
print(os.getcwd())
csv_path = 'result_retrieve_left-and-right_x_50_2016_modified.csv'

parquet_path = 'result_retrieve_left-and-right_x_50_2016_modified.parquet'
# --- Load the modified files ---
print("Loading modified files into new DataFrames...")
df_csv = pd.read_csv(csv_path)
df_parquet = pd.read_parquet(parquet_path)

print("Modified files loaded successfully. Here is a preview of the data:")
display(df_csv.head())
# --- Compare file size and DataFrame shape ---

# Get file sizes
csv_size_bytes = os.path.getsize(csv_path)
parquet_size_bytes = os.path.getsize(parquet_path)

# Get DataFrame shapes
csv_rows, csv_cols = df_csv.shape
parquet_rows, parquet_cols = df_parquet.shape

# Print comparison
print("--- File and DataFrame Comparison ---")
print("\nCSV File:")
print(f"  - File Path: {csv_path}")
print(f"  - Size on disk: {csv_size_bytes / 1024:.2f} KB")
print(f"  - Shape: {csv_rows} rows, {csv_cols} columns")

print("\nParquet File:")
print(f"  - File Path: {parquet_path}")
print(f"  - Size on disk: {parquet_size_bytes / 1024:.2f} KB")
print(f"  - Shape: {parquet_rows} rows, {parquet_cols} columns")

# Highlight the size difference
size_difference = (csv_size_bytes - parquet_size_bytes) / csv_size_bytes * 100
print(f"\nNote: The Parquet file is {size_difference:.2f}% smaller than the CSV file.")
# --- Obtain a statistical description of the DataFrame ---
# (We only need to run this on one DataFrame, as they contain identical data)

print("--- Statistical Description ---")
df_parquet.info()
display(df_parquet.describe(include='all'))
# --- Create average values for x, y, and z columns ---

# Define the columns to group by and the columns to aggregate
grouping_cols = ['fact_id', 'side', 'joint', 'variable']
value_cols = ['value_x', 'value_y', 'value_z']

print(f"Grouping by {grouping_cols} and calculating the mean of {value_cols}...")

# Perform the groupby and aggregation.
# .reset_index() converts the grouped columns back into regular columns.
df_agg = df_parquet.groupby(grouping_cols)[value_cols].mean().reset_index()

# Rename columns for clarity in the database
df_agg.rename(columns={
    'value_x': 'avg_x',
    'value_y': 'avg_y',
    'value_z': 'avg_z'
}, inplace=True)

print("\nPreview of the final data to be loaded:")
display(df_agg.head())
#------------------------------------------------------------------
"""
Script para limpieza, transformación y análisis de datos de articulaciones.
Se trabaja sobre un DataFrame inicial (`df_csv`) y se generan archivos en CSV
y Parquet con datos filtrados de la articulación 'Hip'. Además, se realizan
operaciones estadísticas avanzadas con pandas.
"""

import os
import pandas as pd


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame eliminando filas con valores nulos en value_x, value_y, value_z.

    Args:
        df (pd.DataFrame): DataFrame original.

    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    columnas_validas = ["value_x", "value_y", "value_z"]
    missing_counts = df[columnas_validas].isna().sum()
    print("Número de valores faltantes por columna:")
    print(missing_counts)

    df_clean = df.dropna(subset=columnas_validas)

    print(f"Filas originales: {len(df)}")
    print(f"Filas después de limpiar: {len(df_clean)}")

    missing_after = df_clean[columnas_validas].isna().sum()
    print("Valores faltantes después de limpiar:")
    print(missing_after)

    return df_clean


def eliminar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina columnas no necesarias.

    Args:
        df (pd.DataFrame): DataFrame limpio.

    Returns:
        pd.DataFrame: DataFrame con columnas eliminadas.
    """
    columnas_a_eliminar = ["sd_x", "sd_y", "sd_z", "md_x", "md_y", "md_z"]
    df_final = df.drop(columns=columnas_a_eliminar)

    print("Columnas antes de eliminar las no necesarias:")
    print(df.columns)
    print("Columnas después de eliminar las no necesarias:")
    print(df_final.columns)
    print(df_final.head())
    print(df_final.shape)

    return df_final


def filtrar_hip(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra las filas correspondientes a la articulación 'Hip'.

    Args:
        df (pd.DataFrame): DataFrame procesado.

    Returns:
        pd.DataFrame: Subconjunto de datos con joint = 'Hip'.
    """
    df_hip = df[df["joint"] == "Hip"]
    print(f"Número de filas para 'Hip': {len(df_hip)}")
    print(df_hip.shape)
    return df_hip


def guardar_datos(df: pd.DataFrame, nombre_base: str = "hip_data") -> None:
    """
    Guarda los datos en formatos CSV y Parquet, comparando tamaños.

    Args:
        df (pd.DataFrame): DataFrame a guardar.
        nombre_base (str): Nombre base de los archivos.
    """
    csv_path = f"{nombre_base}.csv"
    parquet_path = f"{nombre_base}.parquet"

    df.to_csv(csv_path, index=False)
    df.to_parquet(parquet_path, index=False)

    print(f"Archivo CSV guardado en: {csv_path}")
    print(f"Archivo Parquet guardado en: {parquet_path}")

    csv_size = os.path.getsize(csv_path)
    parquet_size = os.path.getsize(parquet_path)

    csv_kb = csv_size / 1024
    parquet_kb = parquet_size / 1024
    percentage_smaller = ((csv_size - parquet_size) / csv_size) * 100

    print(f"Tamaño CSV: {csv_size} bytes ({csv_kb:.2f} KB)")
    print(f"Tamaño Parquet: {parquet_size} bytes ({parquet_kb:.2f} KB)")
    print(f"El archivo Parquet es {percentage_smaller:.2f}% más pequeño que el CSV.")


def analisis_avanzado(df: pd.DataFrame) -> None:
    """
    Realiza un análisis estadístico agrupado sobre el DataFrame.

    Args:
        df (pd.DataFrame): DataFrame cargado desde Parquet o limpio.
    """
    agg_std = df.groupby(["side", "variable"])[["value_x", "value_y", "value_z"]].std()
    print("Desviación estándar agrupada por side y variable:")
    print(agg_std)

    # Variable con mayor std de value_x en el lado 'L'
    max_var_L = agg_std.loc["L", "value_x"].idxmax()
    max_val_L = agg_std.loc["L", "value_x"].max()
    print(f"Variable con mayor std de value_x en L: {max_var_L} ({max_val_L})")

    # fact_id con valor máximo en value_y
    idx_max_val_y = df["value_y"].idxmax()
    fact_id_max_y = df.loc[idx_max_val_y, "fact_id"]
    print(f"fact_id con el valor máximo en value_y: {fact_id_max_y}")


def main():
    """Ejecuta todo el flujo de procesamiento de datos."""

    # Limpieza de datos
    df_cleaned = limpiar_datos(df_csv)

    # Eliminación de columnas innecesarias
    df_final = eliminar_columnas(df_cleaned)

    # Filtrar articulación Hip
    df_hip = filtrar_hip(df_final)

    # Guardar resultados
    guardar_datos(df_hip, "hip_data")

    # Cargar Parquet para análisis avanzado
    df_parquet = pd.read_parquet("hip_data.parquet")

    # Análisis avanzado
    analisis_avanzado(df_parquet)


if __name__ == "__main__":
    main()

