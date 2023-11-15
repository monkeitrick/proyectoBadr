import pandas as pd

def colocarPalabra(atril,palabra,cordenada,direccion,tablero):
    loContiene=True
    atrilInterno=atril
    letrasTablero=[]
    indice=0
    row,col=cordenada
    if direccion.lower()=='v':
        dondeTermina=col+len(palabra)
    else:
        dondeTermina=row+len(palabra) 
    if dondeTermina<15:
        if (tablero != '').any().any()==False:
            for letra in palabra:
                tablero.iloc[7,7]=letra
                if direccion.lower()=='v':
                    col+=1
                else:
                    row+=1
        else:
              
    else:
        print("La palabra no cabe, intenta con una mas pequeña")
        
        
        
        """while indice<len(palabra):
            if tablero.iloc[row,col]!='':
                letrasTablero.append(tablero.iloc[row,col])
                if direccion.lower()=='v':
                    col+=1
                else:
                    row+=1
            indice+=1
        for letra in atrilInterno:
            if letra in letrasTablero:
                letrasTablero.pop(letra)
            elif letra in palabra:
                atrilInterno.pop(letra)
            else:
                loContiene=False
        if loContiene==True:
            row,col=cordenada
            for letra in palabra:
                tablero.iloc[row,col]=letra
                if direccion.lower()=='v':
                    col+=1
                else:
                    row+=1"""