import pandas as pd
import Libreriafunciones
# Crear un DataFrame vacío de 15x15
tablero = pd.DataFrame(index=range(15), columns=range(15),data='')

totalPalabras=0
totalFichas=0
Libreriafunciones.mostrarTablero(tablero)