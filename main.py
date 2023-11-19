import Libreriafunciones
import numpy as np
import pandas as pd
menuPrincipal=Libreriafunciones.menuPrincipal()
menuJuego=Libreriafunciones.menuJuego()
mensajeBienvenida=Libreriafunciones.ayudaBienvenida()

tablero = pd.DataFrame(index=range(15), columns=range(15),data=' ')
bolsaDeFichas={}
Libreriafunciones.crearBolsa(bolsaDeFichas)
atrilJugador=[] 
Libreriafunciones.cargarAtril(atrilJugador,bolsaDeFichas)
score=0
usuario=""
libreriaPalabras=[]
puntuaciones={}
Libreriafunciones.obtenerPuntuaciones(puntuaciones)

print(mensajeBienvenida)
seleccionPrincipal=input(menuPrincipal)
# try:
valorMenuPrincipal = int(seleccionPrincipal)
while(seleccionPrincipal!="8"):
    if seleccionPrincipal=="1":
        while usuario=="":
            usuario=input("Introduce tu usuario/Nombre: ")
        print("Bienvenido al juego {}".format(usuario))
    elif seleccionPrincipal=="2":
        if usuario!="":
            Libreriafunciones.mostrarTablero(tablero)
            Libreriafunciones.mostrarTablero(atrilJugador)
            seleccionJuego=input(menuJuego)
            while(seleccionJuego!="7"):
                if seleccionJuego=="1":
                    print()
                elif seleccionJuego=="2":
                    palabra=input("introduce la palabra")
                    cordenada=input("introduce las cordenadas(Numero,Numero)")
                    direccion=input("introduce la direccion")
                    score+=Libreriafunciones.colocarPalabra(atrilJugador,palabra,cordenada,direccion,tablero,libreriaPalabras)
                    Libreriafunciones.cargarAtril(atrilJugador,bolsaDeFichas)
                    Libreriafunciones.mostrarTablero(tablero)
                    Libreriafunciones.mostrarTablero(atrilJugador)
                elif seleccionJuego=="3":
                    Libreriafunciones.mostrarTablero(atrilJugador)
                elif seleccionJuego=="4":
                    print("Tu Puntuacuion es: ",score)
                elif seleccionJuego=="5":
                    Libreriafunciones.mostrarPuntuaciones(puntuaciones)
                elif seleccionJuego=="6":
                    print()
                else:
                    print("Tienes que introducir un valor entre 1 y 7")
                seleccionJuego=input(menuJuego)
        else:
            print("Primero identificate")
    elif seleccionPrincipal=="3":
        print()
        print(Libreriafunciones.csvADataframePuntuaciones())
        print()
    elif seleccionPrincipal=="4":
        print()
        print(Libreriafunciones.csvADataframeJugadas())
        print()
    elif seleccionPrincipal=="5":
        print()
    elif seleccionPrincipal=="6":
        print()
    elif seleccionPrincipal=="7":
        print()
    else:
        print("Tienes que introducir un valor entre 1 y 8")
    seleccionPrincipal=input(menuPrincipal)
# except ValueError:
#     print("Tienes que introducir un valor numerico")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """menuPrincipal=
(1)IDENTIFICARUSUARIO: Introduce tu nombre de usuario por el que serás conocido en el juego
(2)JUGAR: Comenzar el juego una vez identificado el usuario
(3)MOSTRARPUNTUACIONES: Muestra los datos de todas las puntuaciones obtenidas por todos los usuarios en un Dataframe
(4)MOSTRARJUGADAS: Muestra los datos de todas las jugadas realizadas por todos los usuarios en un Dataframe
(5)MOSTRARGRAFICO1: Muestra el grupo de tres gráficos, subset de graficos. 
(6)MOSTRARGRAFICO2: Muestra el Histograma con las puntuaciones del usuario
(7)MOSTRARGRAFICO3: Muestra el grafico de tarta con la información del % de las partidas ganadas y las perdidas. 
(8)SALIR: Para salir del menú y del aplicativo.
"""
"""menuJuego=
(1)MOSTRARAYUDA: Muestra las diferentes opciones de ayuda.
(2)INTRODUCIRPALABRA: Para introducir una nueva palabra.
(3)MISFICHAS: Para ver las fichas.
(4)MIPUNTUACION: Para ver mi puntuación.
(5)PUNTOSDEFICHAS: Para ver la puntuación de las fichas.
(6)PALABRADEAYUDA: Para obtener posibles palabras.
(7)SALIRJUEGO: Para salir del juego y volver al menú principal.
"""