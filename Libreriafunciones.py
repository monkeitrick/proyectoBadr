import pandas as pd
import os
import numpy as np
#Meto en la variable la ruta en la cual esta el proyecto
directorio_actual = os.getcwd()

#funcion para devolver el contenido del archivo mensajes_bienvenida.txt
def ayudaBienvenida():
    rutaArchivoBienvenida = os.path.join(directorio_actual, "Recursos", "mensajes_bienvenida.txt")
    with open(rutaArchivoBienvenida, "r") as archivo:
        mensajeBienvenida= archivo.read()
    return mensajeBienvenida

#funcion para devolver el contenido del archivo menu_juego.txt
def menuPrincipal():
    ruta_archivo_menuTXT = os.path.join(directorio_actual, "Recursos", "menu_juego.txt")
    with open(ruta_archivo_menuTXT, "r") as archivo:
        menuPrincipal= archivo.read()
    return menuPrincipal


#funcion para devolver el contenido del archivo mensajes_opciones_juego.txt
def menuJuego():
    ruta_archivo_juegoTXT= os.path.join(directorio_actual, "Recursos", "mensajes_opciones_juego.txt")
    with open(ruta_archivo_juegoTXT, "r") as archivo:
        menuJuego= archivo.read()
    return menuJuego

#Funcion para mostrar un dataframe
def mostrarTablero(df):
    print(df)

#Funcion para introducir palabras en tablero con distintas comprobaciones,que devuelve los puntos obtenidos en la operacion
def colocarPalabra(atril,palabra,cordenada,direccion,tableroExterno,libreriaPalabras):
    #Inicializo variables que utilizare mas adelante
    coleccionPuntos={}
    puntos=0
    obtenerPuntuaciones(coleccionPuntos)
    tablero=tableroExterno
    loContiene=True
    atrilInterno=atril
    row,col=cordenada.split(',')
    #Miro si la palabra que estoy intentando introducir cabe en el dataframe
    if direccion.lower()=='v':
        dondeTermina=int(col)+len(palabra)
    else:
        dondeTermina=int(row)+len(palabra) 
    if dondeTermina<15:
        #Miro si el tablero esta vacio para ahorrarme la comprobacion de que tengan que estar siempre concatenadas, ya que la primera palabra siempre se introduce sola
        #y ademas siempre es en 7,7
        if (tablero != ' ').any().any()==False:
            col=7
            row=7
            contador=0
            letrasBorrar=[]
            #Miro si tengo las letras en el atril y voy guardando en letrasBorrar las letras a borrar
            for letra in palabra.upper():
                if letra in atrilInterno:
                    letrasBorrar.append(letra)
                else:
                    loContiene=False
                contador+=1
            #Si tengo las letras suficientes en mi atril borro las letras del atril e introduzco la palabra en el tablero
            if loContiene==True:
                for letra in palabra:
                    atrilInterno.remove(letra.upper())
                    tablero.iloc[row-1,col-1]=letra.upper()
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
                print("No hay suficientes letras para introducir la palabra")
                return 0
        else:
            #Miro en que direccion voy para mirar hacia que lado tengo que hacer comprobaciones
            if direccion.lower()=='v':
                #Miro que la palabra tenga sentido dentro del tablero(que no tenga letras antes o despues)
                if tablero.iloc[int(row)-1,int(col)-2]==' ' and tablero.iloc[int(row)-1,int(col)+len(palabra)+1-1]==' ':
                    contador=0
                    letrasBorrar=[]
                    letraEnTablero=False
                    #Miro si tengo las letras en el atril o en el tablero y voy guardando en letrasBorrar las letras a borrar
                    for letra in palabra.upper():
                        if letra == tablero.iloc[int(row)-1,int(col)+contador-1]:
                            letraEnTablero=True
                        elif letra in atrilInterno:
                            letrasBorrar.append(letra)
                        else:
                            loContiene=False
                        contador+=1
                    #Si tengo las letras suficientes en mi atril borro las letras del atril e introduzco la palabra en el tablero
                    if loContiene==True:
                        if letraEnTablero==True:
                            for letra in letrasBorrar:
                                atrilInterno.remove(letra.upper())
                            atril=atrilInterno
                            row,col=cordenada.split(',')
                            for letra in palabra:
                                tablero.iloc[int(row)-1,int(col)-1]=letra.upper()
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
            #Miro en que direccion voy para mirar hacia que lado tengo que hacer comprobaciones
                if tablero.iloc[int(row)-2,int(col)-1]==' ' and tablero.iloc[int(row)+len(palabra)+1-1,int(col)-1]==' ':
                    contador=0
                    letrasBorrar=[]
                    letraEnTablero=False
                    #Miro que la palabra tenga sentido dentro del tablero(que no tenga letras antes o despues)
                    for letra in palabra.upper():
                        if letra == tablero.iloc[int(row)+contador-1,int(col)-1]:
                            letraEnTablero=True
                        elif letra in atrilInterno:
                            letrasBorrar.append(letra)
                        else:
                            loContiene=False
                        contador+=1
                    #Si tengo las letras suficientes en mi atril borro las letras del atril e introduzco la palabra en el tablero
                    if loContiene==True:
                        if letraEnTablero==True:
                            for letra in letrasBorrar:
                                atrilInterno.remove(letra.upper())
                            atril=atrilInterno
                            row,col=cordenada.split(',')
                            for letra in palabra:
                                tablero.iloc[int(row)-1,int(col)-1]=letra.upper()
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

#Funcion que devuelve el contenido del archivo diccionario.txt
def obtenerDiccionario():
    ruta_archivo_diccionarioTXT = os.path.join(directorio_actual, "Recursos", "diccionario.txt")
    with open(ruta_archivo_diccionarioTXT, "r", encoding="utf-8") as archivo:
        menuPrincipal= archivo.read()
    return menuPrincipal

#Funcion que devuelve el contenido del archivo diccionario_reduc_sin_tildes.txt
def obtenerDiccionarioCorto():
    ruta_archivo_diccionarioTXT = os.path.join(directorio_actual, "Recursos", "diccionario_reduc_sin_tildes.txt")
    with open(ruta_archivo_diccionarioTXT, "r", encoding="utf-8") as archivo:
        menuPrincipal = archivo.read()
    return menuPrincipal

#Funcion que devuelve si una palabra esta en el diccionario(que tiene significado)
def validarPalabra(palabra):
    diccionario=obtenerDiccionario()
    lineas = diccionario.split('\n')
    for palabraInterna in lineas:
        if palabra == palabraInterna:
            return True
    return False
    
#Funcion que devuelve si una palabra esta en el diccionario(que tiene significado)
def validarPalabraCorto(palabra):
    diccionario=obtenerDiccionarioCorto()
    lineas = diccionario.split('\n')
    for palabraInterna in lineas:
        if palabra == palabraInterna:
            return True
    return False

#Funcion que devuelve si la palabra esta vacia
def esPalabraVacia(palabra):
    if palabra=='':
        return True
    else:
        return False
    
#Funcion que añade una ficha a una coleccion, ambas tiene que introducirlas el usuario
def aniadirFicha(ficha,coleccion):
    coleccion.append(ficha)

#Funcion que añade una ficha a una coleccion varias veces, ambas tiene que introducirlas el usuario
def aniadirFichas(ficha,repeticiones,coleccion):
    contador=0
    while contador < repeticiones:
        aniadirFicha(ficha,coleccion)
        contador+=1
        
#Funcion que que creea una bolsa de fichas utilizando el csv bolsa_de_fichas.csv
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

#funcion que muestra la cantidad de fichas que quedan en la bolsa de fichas
def mostrarFichas(coleccion):
    for letra in coleccion.keys():
        cantidad=coleccion[letra]
        print(letra,",",cantidad)

#Funcion para seleccionar una ficha random de la bolsa
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

#Funcion que carga el atril siempre con 7 fichas,da igual con cuantas entre
def cargarAtril(atril,bolsa):
    while len(atril) < 7:
        letra=tomarFichaRandom(bolsa)
        aniadirFichas(letra,1,atril)
#Funvion para obtener el valor de cada ficha e introducirlo en la coleccion que se le pasa
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
#Funcion para mostrar la coleccionq que se le pasa
def mostrarPuntuaciones(coleccion):
    for letra in coleccion.keys():
        cantidad=coleccion[letra]
        print(letra,",",cantidad)
#Funcion que devuelve los puntos que vale la letras que se le pasa
def getPuntos(letra,puntos):
    return puntos[letra.upper()]
#funcion que coge el archivo puntuaciones.csv y lo convierte en un dataframe
def csvADataframePuntuaciones():
    directorio_actual = os.getcwd()
    ruta_archivo_csv = os.path.join(directorio_actual, "Recursos", "puntuaciones.csv")
    try:
        df = pd.read_csv(ruta_archivo_csv, header=None, names=["Usuario", "Nº de partida", "Puntos totales", "Nº total palabras", "Max puntos palabra", "Partida Ganada(S/N)", "Palabra ganadora"], encoding='ISO-8859-1', delimiter=';', skiprows=1)
        return df
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    
#funcion que coge el archivo jugadas.csv y lo convierte en un dataframe    
def csvADataframeJugadas():
    directorio_actual = os.getcwd()
    ruta_archivo_csv = os.path.join(directorio_actual, "Recursos", "jugadas.csv")
    try:
        df = pd.read_csv(ruta_archivo_csv, header=None, names=["Usuario", "Nº de partida", "Palabra", "Puntos de palabra", "Longitud Palabra", "Nº de vocales", "Nº de consonantes", "Vertical u Horizontal (V/H)", "Palabra ganadora (S/N)"], encoding='ISO-8859-1', delimiter=';', skiprows=1)
        return df
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None

#Funcion para quitar las fichas del atril que le pasa
def quitarFichas(fichas,atril):
    noContiene=True
    for letra in fichas.upper():
        if letra in atril:
            continue
        else:
            noContiene=False
    if noContiene==True:
        for letra in fichas.upper():
            atril.remove(letra)
        return True
    else:
        print("No tienes esas letras en el atril")
        return False
