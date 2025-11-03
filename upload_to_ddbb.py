import psycopg2
import os

def import_csv_to_postgres_copy(csv_filepath, table_name, db_details):
    try:
        conn = psycopg2.connect(**db_details)
        cur = conn.cursor()

        with open(csv_filepath, 'r') as f:
            # Omitir la fila de encabezado si el CSV la posee.
            # next(f) 
            cur.copy_from(f, table_name, sep=',') 
        
        conn.commit()
        print(f"Datos de {csv_filepath} importados exitosamente a {table_name}.")

    except Exception as e:
        print(f"Error durante la importación: {e}")
        conn.rollback() # Revertir la transacción en caso de error.
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Ejemplo de uso:
db_config = {
    "host": "localhost",
    "database": "nombre_de_tu_base_de_datos",
    "user": "tu_nombre_de_usuario",
    "password": "tu_contraseña"
}

# Directorio que contiene los archivos CSV.
csv_folder = "ruta/a/tu/carpeta/csv"
target_table = "nombre_de_tu_tabla"

# Iterar sobre todos los archivos en el directorio.
for filename in os.listdir(csv_folder):
    if filename.endswith(".csv"):
        csv_file_path = os.path.join(csv_folder, filename)
        import_csv_to_postgres_copy(csv_file_path, target_table, db_config)