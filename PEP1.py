i=0
mayor = ''
contadormayor = 0
print("Recuerda, ingresa '.' para salir")
while i==0:
    palabra = input("Ingrese  la palabra:\n")
    lista = list(palabra)
    posicion = 0
    contador = 0
    while posicion<len(palabra):
        if lista[posicion]:
            if posicion+1 != len(palabra) and lista[posicion]+lista[posicion+1] == 'CH':
                posicion+=1
                contador+=5
            elif posicion+1 != len(palabra) and (lista[posicion]+lista[posicion+1] == 'LL' or lista[posicion]+lista[posicion+1] == 'RR'):
                posicion+=1
                contador+=8
            elif lista[posicion] in ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U']:
                contador+=1
            elif lista[posicion] in ['D', 'G']:
                contador+=2
            elif lista[posicion] in ['B','C', 'M', 'P']:
                contador+=3
            elif lista[posicion] in ['F', 'H', 'Y']:
                contador+=4
            elif lista[posicion] == 'Q':
                contador+=5
            elif lista[posicion] in ['J', 'Ñ', 'X']:
                contador+=8
            elif lista[posicion] == 'Z':
                contador+=10
        posicion+=1
    if palabra == ".":
        i=1
    if contadormayor < contador:
        contadormayor = contador
        mayor = palabra
        
print("La palabra "+mayor+" es la mas alta con "+str(contadormayor)+" puntos")
