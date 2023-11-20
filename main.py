import Libreriafunciones
import numpy as np
import pandas as pd
#Meto en variables el contenido de distintos archivos asi los puedo usar mas facil mas adelante
menuPrincipal=Libreriafunciones.menuPrincipal()
menuJuego=Libreriafunciones.menuJuego()
mensajeBienvenida=Libreriafunciones.ayudaBienvenida()
#Inicializo y relleno distintas variables que utilizare mas adelante
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
vecesPasado=0
print(mensajeBienvenida)
seleccionPrincipal=input(menuPrincipal)
try:
    valorMenuPrincipal = int(seleccionPrincipal)
    seleccionJuego=0
    #Mientras que el usuario introduzca un valor que sea distinto a 8 no sale, pero siempre tiene que ser entre 1 y 8
    while(seleccionPrincipal!="8"):
        if seleccionPrincipal=="1":
            #Mientras el usuario no sea distinto a "" no sale
            while usuario=="":
                usuario=input("Introduce tu usuario/Nombre: ")
            print("Bienvenido al juego {}".format(usuario))
        elif seleccionPrincipal=="2":
            #Comprueba que el usuario este "Logueado"
            if usuario!="":
                #Muestro tablero y atril
                Libreriafunciones.mostrarTablero(tablero)
                Libreriafunciones.mostrarTablero(atrilJugador)
                seleccionJuego=input(menuJuego)
                #Mientras que el usuario introduzca un valor que sea distinto a 9 no sale, pero siempre tiene que ser entre 1 y 9
                while(seleccionJuego!="9"):
                    if seleccionJuego=="1":
                        #No se que hay que hacer aqui
                        print()
                    elif seleccionJuego=="2":
                        #Le pido la informacion necesaria al jugador para introducir la palabra
                        palabra=input("introduce la palabra: ")
                        cordenada=input("introduce las cordenadas(Numero,Numero): ")
                        direccion=input("introduce la direccion(h,v): ")
                        if Libreriafunciones.esPalabraVacia(palabra)==True:
                            print("La palabra no puede estar vacia")
                        elif Libreriafunciones.validarPalabra(palabra)==True:
                            #Introduzco la palabra
                            score+=Libreriafunciones.colocarPalabra(atrilJugador,palabra,cordenada,direccion,tablero,libreriaPalabras)
                            vecesPasado=0
                            #Cargo el atril otra vez
                            Libreriafunciones.cargarAtril(atrilJugador,bolsaDeFichas)
                            #Muestro el atril y el tablero otra vez
                            Libreriafunciones.mostrarTablero(tablero)
                            Libreriafunciones.mostrarTablero(atrilJugador)
                        else:
                            print("La palabra introducida no existe")
                    elif seleccionJuego=="3":
                        #Muestro el atril
                        Libreriafunciones.mostrarTablero(atrilJugador)
                    elif seleccionJuego=="4":
                        #Muestro la puntuacion de la partida
                        print("Tu Puntuacuion es: ",score)
                    elif seleccionJuego=="5":
                        #Muestro todas las puntuaciones de cada letra
                        Libreriafunciones.mostrarPuntuaciones(puntuaciones)
                    elif seleccionJuego=="6":
                        print()
                    elif seleccionJuego=="7":
                        #Miro las condiciones para ganar y perder y muestro el resultado, tambien reinicio las variables para dejar el juego para jugar otra vez
                        if score==75 and (len(atrilJugador)>5 and len(bolsaDeFichas)==0 ) and len(atrilJugador)==0 and seleccionJuego<3:
                            print("Has ganado, Bien jugado")
                        else:
                            print("Que pena, Has perdido")
                        Libreriafunciones.crearBolsa(bolsaDeFichas)
                        atrilJugador=[]
                        Libreriafunciones.cargarAtril(atrilJugador,bolsaDeFichas)
                        score=0
                        libreriaPalabras=[]
                        Libreriafunciones.obtenerPuntuaciones(puntuaciones)
                        tablero = pd.DataFrame(index=range(15), columns=range(15),data=' ')
                    elif seleccionJuego=="8":
                        #Borro las letras del atril que el usuario quiere, y le sumo una a vecesPasado
                        fichasQuitar=input("introduce las fichas: ")
                        quitadoFichas=Libreriafunciones.quitarFichas(fichasQuitar,atrilJugador)
                        if quitadoFichas==True:
                            Libreriafunciones.cargarAtril(atrilJugador,bolsaDeFichas)
                            vecesPasado+=1
                    else:
                        print("Tienes que introducir un valor entre 1 y 9")
                    #Si VecesPasado pasa a valer 3 lo redirecciono a terminarJuego
                    if(vecesPasado<3):
                        seleccionJuego=input(menuJuego)
                    else:
                        seleccionJuego=7
                    #Si Se ha terminado el juego lo redirecciono a SalirJuego
                    if seleccionJuego==7:
                        seleccionJuego=9
                    else:
                        seleccionJuego=input(menuJuego)
            else:
                print("Primero identificate")
            
        elif seleccionPrincipal=="3":
        #Muestro todas las puntuaciones de partidas 
            print()
            print(Libreriafunciones.csvADataframePuntuaciones())
            print()
        elif seleccionPrincipal=="4":
        #Muestro todas las jugadas de todas las partidas
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
except ValueError:
    print("Tienes que introducir un valor numerico")
