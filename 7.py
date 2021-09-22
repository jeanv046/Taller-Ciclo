
aux = True
compra = []
while (aux):
    precio = float(input('Cual es el precio del articulo: '))
    cantidad = int(input('Cantidad de ese producto: '))
    compra.append([precio, cantidad])
    
    desicion = input('Desea saber su total? (Si - no)')
    if desicion == 'si' or desicion == 'Si':
        aux = False
suma = 0 
for articulo in compra:
    resultado = articulo[0] * articulo[1]
    suma = suma + resultado

print(f'Su total de la compra es {suma}')