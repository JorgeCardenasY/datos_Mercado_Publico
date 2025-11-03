import pandas as pd
import numpy as np
import os

anio = [2020, 2021, 2022, 2023, 2024, 2025]
mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 , 12]

oc = "https://transparenciachc.blob.core.windows.net/oc-da/anio-mes.zip"

for a in anio:
    for m in mes:
        url = oc.replace("anio", str(a)).replace("mes", str(m))
        os.system(f"wget -O ord_compra/{str(a)}-{str(m)}.zip {url}")
        os.system(f"unzip ord_compra/{str(a)}-{str(m)}.zip -d ord_compra/")
        os.system(f"rm ord_compra/{str(a)}-{str(m)}.zip")

print("La descarga de las órdenes de compra para los años y meses seleccionados ha finalizado")