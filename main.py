import os
directorio_actual = os.getcwd()
ruta_archivo_menuTXT = os.path.join(directorio_actual,"proyectoBadr", "Recursos", "menu_juego.txt")
ruta_archivo_juegoTXT= os.path.join(directorio_actual,"proyectoBadr", "Recursos", "mensajes_opciones_juego.txt")
with open(ruta_archivo_menuTXT, "r") as archivo:
    menuPrincipal= archivo.read()
with open(ruta_archivo_juegoTXT, "r") as archivo:
    menuJuego= archivo.read()


seleccionPrincipal=input(menuPrincipal)
try:
    valorMenuPrincipal = int(seleccionPrincipal)
    while(seleccionPrincipal!="8"):
        if seleccionPrincipal=="1":
            print()
        elif seleccionPrincipal=="2":
            seleccionJuego=input(menuJuego)
            while(seleccionJuego!="7"):
                if seleccionJuego=="1":
                    print()
                elif seleccionJuego=="2":
                    print()
                elif seleccionJuego=="3":
                    print()
                elif seleccionJuego=="4":
                    print()
                elif seleccionJuego=="5":
                    print()
                elif seleccionJuego=="6":
                    print()
                else:
                    print("Tienes que introducir un valor entre 1 y 7")
                seleccionPrincipal=input(menuPrincipal)
        elif seleccionPrincipal=="3":
            print()
        elif seleccionPrincipal=="4":
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