import pandas as pd

def colocarPalabra(atril,palabra,cordenada,direccion,tablero):
    loContiene=True
    atrilInterno=atril
    row,col=cordenada.split(',')
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
            return True
        else:
            if direccion.lower()=='v':
                if tablero.iloc[row,col-1]==' ' and tablero.iloc[row,col+len(palabra)+1]==' ':
                    contador=0
                    for letra in atrilInterno:
                        if letra == tablero.iloc[row,col+contador]:
                            continue
                        elif letra in palabra:
                            atrilInterno.pop(letra)
                        else:
                            loContiene=False
                        contador+=1
                    if loContiene==True:
                        atril=atrilInterno
                        row,col=cordenada
                        for letra in palabra:
                            tablero.iloc[row,col]=letra
                            col+=1
                    return True 
                else:
                    print("Error no puedes introducir una palabra dentro de otra que no tenga ningun significado")
                    return False
            else:
                if tablero.iloc[row-1,col]==' ' and tablero.iloc[row+len(palabra)+1,col]==' ':
                    contador=0
                    for letra in atrilInterno:
                        if letra == tablero.iloc[row+contador,col]:
                            continue
                        elif letra in palabra:
                            atrilInterno.pop(letra)
                        else:
                            loContiene=False
                        contador+=1
                    if loContiene==True:
                        atril=atrilInterno
                        row,col=cordenada
                        for letra in palabra:
                            tablero.iloc[row,col]=letra
                            col+=1
                    return True 
                else:
                    print("Error no puedes introducir una palabra dentro de otra que no tenga ningun significado")
                    return False
    else:
        print("La palabra no cabe, intenta con una mas pequeña")
        return False
        
        
        
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