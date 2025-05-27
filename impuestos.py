consumo=int(input("Ingrese el consumo del cliente: "))
if consumo <= 100:
    print("no paga impuestos")
elif consumo <= 200 and consumo > 101:
    print("0,5 por cada unidad consumida")
elif consumo > 201:
    print("0,7 por cada unidad consumida")