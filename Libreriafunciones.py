import pandas as pd
import os
import numpy as np
directorio_actual = os.getcwd()

def ayudaBienvenida():
    rutaArchivoBienvenida = os.path.join(directorio_actual, "Recursos", "mensajes_bienvenida.txt")
    with open(rutaArchivoBienvenida, "r") as archivo:
        mensajeBienvenida= archivo.read()
    return mensajeBienvenida

def menuPrincipal():
    ruta_archivo_menuTXT = os.path.join(directorio_actual, "Recursos", "menu_juego.txt")
    with open(ruta_archivo_menuTXT, "r") as archivo:
        menuPrincipal= archivo.read()
    return menuPrincipal


def menuJuego():
    ruta_archivo_juegoTXT= os.path.join(directorio_actual, "Recursos", "mensajes_opciones_juego.txt")
    with open(ruta_archivo_juegoTXT, "r") as archivo:
        menuJuego= archivo.read()
    return menuJuego

def mostrarTablero(df):
    print(df)


def colocarPalabra(atril,palabra,cordenada,direccion,tableroExterno,libreriaPalabras):
    coleccionPuntos={}
    puntos=0
    obtenerPuntuaciones(coleccionPuntos)
    tablero=tableroExterno
    loContiene=True
    atrilInterno=atril
    row,col=cordenada.split(',')
    if direccion.lower()=='v':
        dondeTermina=int(col)+len(palabra)
    else:
        dondeTermina=int(row)+len(palabra) 
    if dondeTermina<15:
        #poner un espacio en tablero!=' '
        if (tablero != ' ').any().any()==False:
            col=7
            row=7
            for letra in palabra:
                atrilInterno.remove(letra)
                tablero.iloc[row-1,col-1]=letra
                puntos=puntos+getPuntos(letra,coleccionPuntos)
                print(puntos)
                if direccion.lower()=='v':
                    col+=+1
                else:
                    row+=1
            atril=atrilInterno
            libreriaPalabras.append(palabra)
            return puntos
        else:
            if direccion.lower()=='v':
                if tablero.iloc[int(row)-1,int(col)-2]==' ' and tablero.iloc[int(row)-1,int(col)+len(palabra)+1-1]==' ':
                    contador=0
                    letrasBorrar=[]
                    letraEnTablero=False
                    for letra in palabra:
                        if letra == tablero.iloc[int(row)-1,int(col)+contador-1]:
                            letraEnTablero=True
                        elif letra in atrilInterno:
                            letrasBorrar.append(letra)
                        else:
                            loContiene=False
                        contador+=1
                    if loContiene==True:
                        if letraEnTablero==True:
                            for letra in letrasBorrar:
                                atrilInterno.remove(letra)
                            atril=atrilInterno
                            row,col=cordenada.split(',')
                            for letra in palabra:
                                tablero.iloc[int(row)-1,int(col)-1]=letra
                                puntos+=getPuntos(letra,coleccionPuntos)
                                col=int(col)+1
                            libreriaPalabras.append(palabra)
                            return puntos
                        else:
                            print("Las palabras tienen que estas conectadas entre ellas")
                            return 0   
                    else:
                        print("No hay suficientes letras para introducir la palabra")
                        return 0
                else:
                    print("Error no puedes introducir una palabra dentro de otra que no tenga ningun significado")
                    return 0
            else:
                if tablero.iloc[int(row)-2,int(col)-1]==' ' and tablero.iloc[int(row)+len(palabra)+1-1,int(col)-1]==' ':
                    contador=0
                    letrasBorrar=[]
                    letraEnTablero=False
                    for letra in palabra:
                        if letra == tablero.iloc[int(row)+contador-1,int(col)-1]:
                            letraEnTablero=True
                        elif letra in atrilInterno:
                            letrasBorrar.append(letra)
                        else:
                            loContiene=False
                        contador+=1
                    if loContiene==True:
                        if letraEnTablero==True:
                            for letra in letrasBorrar:
                                atrilInterno.remove(letra)
                            atril=atrilInterno
                            row,col=cordenada.split(',')
                            for letra in palabra:
                                tablero.iloc[int(row)-1,int(col)-1]=letra
                                row=int(row)+1
                                puntos+=getPuntos(letra,coleccionPuntos)
                            libreriaPalabras.append(palabra)
                            return puntos
                        else:
                            print("Las palabras tienen que estas conectadas entre ellas")
                            return 0   
                    else:
                        print("No hay suficientes letras para introducir la palabra")
                        return 0
                else:
                    print("Error no puedes introducir una palabra dentro de otra que no tenga ningun significado")
                    return 0
    else:
        print("La palabra no cabe, intenta con una mas pequeña")
        return 0
def obtenerDiccionario():
    ruta_archivo_diccionarioTXT = os.path.join(directorio_actual, "Recursos", "diccionario.txt")
    with open(ruta_archivo_diccionarioTXT, "r", encoding="utf-8") as archivo:
        menuPrincipal= archivo.read()
    return menuPrincipal

def obtenerDiccionarioCorto():
    ruta_archivo_diccionarioTXT = os.path.join(directorio_actual, "Recursos", "diccionario_reduc_sin_tildes.txt")
    with open(ruta_archivo_diccionarioTXT, "r", encoding="utf-8") as archivo:
        menuPrincipal = archivo.read()
    return menuPrincipal

def validarPalabra(palabra):
    diccionario=obtenerDiccionario()
    lineas = diccionario.split('\n')
    for palabraInterna in lineas:
        if palabra == palabraInterna:
            return True
    return False
    
    
def validarPalabraCorto(palabra):
    diccionario=obtenerDiccionarioCorto()
    lineas = diccionario.split('\n')
    for palabraInterna in lineas:
        if palabra == palabraInterna:
            return True
    return False

def esPalabraVacia(palabra):
    if palabra=='':
        return True
    else:
        return False
    
def aniadirFicha(ficha,coleccion):
    coleccion.append(ficha)
    
def aniadirFichas(ficha,repeticiones,coleccion):
    contador=0
    while contador < repeticiones:
        aniadirFicha(ficha,coleccion)
        contador+=1
        
def crearBolsa(coleccion):
    directorio_actual = os.getcwd()
    ruta_archivo_csv = os.path.join(directorio_actual, "Recursos", "bolsa_de_fichas.csv")
    try:
        with open(ruta_archivo_csv, "r") as archivo:
            next(archivo)
            for linea in archivo:
                ficha, repeticiones = linea.split(',')
                coleccion[ficha.replace("\"","")] = int(repeticiones.replace("\n", ""))
    except FileNotFoundError:
        print("El archivo no se encontró.")


def mostrarFichas(coleccion):
    for letra in coleccion.keys():
        cantidad=coleccion[letra]
        print(letra,",",cantidad)
        
def tomarFichaRandom(bolsa):
        if not bolsa:
            print("La bolsa está vacía.")
            return None

        fichas_disponibles = list(bolsa.keys())
        ficha_seleccionada = np.random.choice(fichas_disponibles)
        bolsa[ficha_seleccionada] -= 1

        if bolsa[ficha_seleccionada] == 3:
            del bolsa[ficha_seleccionada]

        return ficha_seleccionada

def cargarAtril(atril,bolsa):
    while len(atril) < 7:
        letra=tomarFichaRandom(bolsa)
        aniadirFichas(letra,1,atril)
        
def obtenerPuntuaciones(coleccion):
    directorio_actual = os.getcwd()
    ruta_archivo_csv = os.path.join(directorio_actual, "Recursos", "puntuacionesLetras.csv")
    try:
        with open(ruta_archivo_csv, "r") as archivo:
            next(archivo)
            for linea in archivo:
                ficha, repeticiones = linea.split(',')
                coleccion[ficha.replace("\"","")] = int(repeticiones.replace("\n", ""))
    except FileNotFoundError:
        print("El archivo no se encontró.")
        
def mostrarPuntuaciones(coleccion):
    for letra in coleccion.keys():
        cantidad=coleccion[letra]
        print(letra,",",cantidad)

def getPuntos(letra,puntos):
    return puntos[letra.upper()]

def csvADataframePuntuaciones():
    directorio_actual = os.getcwd()
    ruta_archivo_csv = os.path.join(directorio_actual, "Recursos", "puntuaciones.csv")
    try:
        df = pd.read_csv(ruta_archivo_csv, header=None, names=["Usuario", "Nº de partida", "Puntos totales", "Nº total palabras", "Max puntos palabra", "Partida Ganada(S/N)", "Palabra ganadora"], encoding='ISO-8859-1', delimiter=';', skiprows=1)
        return df
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    
def csvADataframeJugadas():
    directorio_actual = os.getcwd()
    ruta_archivo_csv = os.path.join(directorio_actual, "Recursos", "jugadas.csv")
    try:
        df = pd.read_csv(ruta_archivo_csv, header=None, names=["Usuario", "Nº de partida", "Palabra", "Puntos de palabra", "Longitud Palabra", "Nº de vocales", "Nº de consonantes", "Vertical u Horizontal (V/H)", "Palabra ganadora (S/N)"], encoding='ISO-8859-1', delimiter=';', skiprows=1)
        return df
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None