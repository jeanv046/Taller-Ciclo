
conjunto = []
datos = int(input('Cuantos datos va a ingresar: '))

for x in range(datos):
    dato = float(input(f'Digita el dato #{x+1}: '))
    conjunto.append(dato)
datomenor = conjunto[0]

for x in conjunto:
    if datomenor > x:
        datomenor = x
print(f'El dato menor en el conjunto de datos es {datomenor}')