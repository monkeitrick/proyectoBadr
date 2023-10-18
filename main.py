seleccionPrincipal=input("""
(1)IDENTIFICARUSUARIO: Introduce tu nombre de usuario por el que serás conocido en el juego
(2)JUGAR: Comenzar el juego una vez identificado el usuario
(3)MOSTRARPUNTUACIONES: Muestra los datos de todas las puntuaciones obtenidas por todos los usuarios en un Dataframe
(4)MOSTRARJUGADAS: Muestra los datos de todas las jugadas realizadas por todos los usuarios en un Dataframe
(5)MOSTRARGRAFICO1: Muestra el grupo de tres gráficos, subset de graficos. 
(6)MOSTRARGRAFICO2: Muestra el Histograma con las puntuaciones del usuario
(7)MOSTRARGRAFICO3: Muestra el grafico de tarta con la información del % de las partidas ganadas y las perdidas. 
(8)SALIR: Para salir del menú y del aplicativo.
""")
seleccionJuego=input("""
(1)MOSTRARAYUDA: Muestra las diferentes opciones de ayuda.
(2)INTRODUCIRPALABRA: Para introducir una nueva palabra.
(3)MISFICHAS: Para ver las fichas.
(4)MIPUNTUACION: Para ver mi puntuación.
(5)PUNTOSDEFICHAS: Para ver la puntuación de las fichas.
(6)PALABRADEAYUDA: Para obtener posibles palabras.
(7)SALIRJUEGO: Para salir del juego y volver al menú principal.
""")
try:
    menuPrincipal = int(seleccionPrincipal)
    while(seleccionPrincipal!=8):
        if seleccionPrincipal==1:
            print()
        elif seleccionPrincipal==2:
            print()
        elif seleccionPrincipal==3:
            print()
        elif seleccionPrincipal==4:
            print()
        elif seleccionPrincipal==5:
            print()
        elif seleccionPrincipal==6:
            print()
        elif seleccionPrincipal==7:
            print()
        else:
            print("Tienes que introducir un valor entre 1 y 8")
except ValueError:
    print("Tienes que introducir un valor numerico")