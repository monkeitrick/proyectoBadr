import pandas as pd
import os

directorio_actual = os.getcwd()
ruta_archivo_fichas = os.path.join(directorio_actual,"proyectoBadr", "Recursos", "bolsa_de_fichas.csv")
df = pd.read_csv(ruta_archivo_fichas)

print(df)