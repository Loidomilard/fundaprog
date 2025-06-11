numeros=input('dame los numero separados por comas:')
numeros=numeros.split(',')
for i in range(len(numeros)):
    numlist=int(numeros[i])
    numeros[i]=numlist
print(numeros)

resultado=0
for i in range(len(numeros)):
    resultado += numeros[i]
print( resultado)

resultado=str(resultado)
#print(len(resultado))  da 2
#if resultado>1:


while len(resultado) > 1:
    suma=0
    for i in range(len(resultado)):
        suma += int(resultado[i] )
    resultado = str(suma)
print(f'el resultador final es {suma}')
#1 el input
#2 ponerlo en una lista y hacerlo str (para poder sumarlo)
#3 recorrer la lista y sumarlo
#4 guardar el resultado en una variable resultado
#5 un while
#6 si el resultado tiene mas de un digito hacer lista y recorrerla y sumar los digitos