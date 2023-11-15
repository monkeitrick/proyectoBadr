import pandas as pd
import os
directorio_actual = os.getcwd()
def crearBolsa():
    ruta_archivo_fichas = os.path.join(directorio_actual,"proyectoBadr", "Recursos", "bolsa_de_fichas.csv")
    df = pd.read_csv(ruta_archivo_fichas)
    return df

def ayudaBienvenida():
    rutaArchivoBienvenida = os.path.join(directorio_actual,"proyectoBadr", "Recursos", "mensajes_bienvenida.txt")
    with open(rutaArchivoBienvenida, "r") as archivo:
        mensajeBienvenida= archivo.read()
    return mensajeBienvenida

def menuPrincipal():
    ruta_archivo_menuTXT = os.path.join(directorio_actual,"proyectoBadr", "Recursos", "menu_juego.txt")
    with open(ruta_archivo_menuTXT, "r") as archivo:
        menuPrincipal= archivo.read()
    return menuPrincipal


def menuJuego():
    ruta_archivo_juegoTXT= os.path.join(directorio_actual,"proyectoBadr", "Recursos", "mensajes_opciones_juego.txt")
    with open(ruta_archivo_juegoTXT, "r") as archivo:
        menuJuego= archivo.read()
    return menuJuego

def mostrarTablero(df):
    print(df)
