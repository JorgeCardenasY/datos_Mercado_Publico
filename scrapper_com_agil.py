import pandas as pd
import numpy as np
import os

anio = [2020, 2021, 2022, 2023, 2024, 2025]
mes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10' , '11' , '12']

com_agil = "https://transparenciachc.blob.core.windows.net/trnspchc/COT_anio-mes.zip"

for a in anio:
    for m in mes:
        url = com_agil.replace("anio", str(a)).replace("mes", str(m))
        os.system(f"wget -O com_agil/{str(a)}-{str(m)}.zip {url}")
        os.system(f"unzip com_agil/{str(a)}-{str(m)}.zip -d com_agil/")
        os.system(f"rm com_agil/{str(a)}-{str(m)}.zip")

print("La descarga de las compras ágiles para los años y meses seleccionados ha finalizado")