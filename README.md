# Proyecto: Scrapers de Datos y Cargador

Este proyecto contiene un conjunto de scripts de Python diseñados para extraer datos de diversas fuentes y cargarlos en una base de datos PostgreSQL.

## Scripts

### `scrapper_com_agil.py`
Este script es responsable de descargar los datos de "compras ágiles". Itera a través de un rango predefinido de años y meses, construye una URL para cada período, descarga un archivo ZIP que contiene los datos, lo descomprime en el directorio `com_agil/` y luego elimina el archivo ZIP descargado.

### `scrapper_licitaciones.py`
Este script descarga los datos de "licitaciones". Similar a `scrapper_com_agil.py`, recorre un rango de años y meses, forma una URL, descarga un archivo ZIP, extrae su contenido en el directorio `licitaciones/` y elimina el archivo ZIP.

### `scrapper_ord_compra.py`
Este script se encarga de la descarga de los datos de "órdenes de compra". Sigue el mismo patrón que los otros scripts de scrapper: itera a través de años y meses, descarga un archivo ZIP desde una URL construida, lo descomprime en el directorio `ord_compra/` y elimina el archivo ZIP.

### `upload_to_ddbb.py`
Este script proporciona la funcionalidad para cargar datos CSV en una base de datos PostgreSQL. Contiene una función `import_csv_to_postgres_copy` que toma la ruta de un archivo CSV, el nombre de una tabla de destino y los detalles de conexión de la base de datos, luego utiliza el método `copy_from` de `psycopg2` para una inserción masiva eficiente. El script también incluye un ejemplo de cómo iterar a través de una carpeta específica de archivos CSV y cargarlos en una tabla de la base de datos. Los usuarios deben configurar las variables `db_config`, `csv_folder` y `target_table` antes de ejecutarlo. <br>
<br>
> jorge@eLabs.cl