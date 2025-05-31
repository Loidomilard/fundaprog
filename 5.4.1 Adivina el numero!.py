numero=int(input("ingrese un numero entre 1 y 100: "))
import random
i = random.randint(1, 100)
while numero != i:
    if numero < i:
        print('el numero secreto es menor')
        print('Intenta de nuevo')
        break
    elif numero > i:
        print('el numero secreto es mayor')
        print('Intenta de nuevo')
        break
    else:
        print('Felicidades, adivinaste el numero secreto:', i)
        break
    