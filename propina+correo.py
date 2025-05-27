#ejercicio 1
total=int(input('Total: '))
propina=int(input('Propina en porcentaje: '))
propina=propina/100
total=total+total*propina
print('Total a pagar: ', total)
#ejercicio 2
primernombre=input('Nombre1: ')
segundonombre=input('Nombre2: ')
primerapellido=input('Apellido1: ')
segundoapellido=input('Apellido2: ')
print(f'El correo que se debe asignar al usuario ingresado es {primernombre}.{primerapellido}@keyinstitute.edu.sv') 
