lista=[1,8,1,1,6,5,6,8,8,4]
lista_sin_repetidos = [] 
for i in lista:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)
print(lista_sin_repetidos)