contra= input('Introduce una contraseña: ')
mayuscula=False
numero = False
for i in contra: #recorre la contraseña
    if i.isdigit():
        numero=True
    if i.isupper():
        mayuscula=True
if len(contra) >= 8 and mayuscula and numero:
    print('Contraseña segura')
else:
    print('Contraseña insegura')