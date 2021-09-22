valor = 0
descuento = 0
valorFinal = 0
cantidadPersonas = int(input("Ingrese la cantidad de personas: "))
for i in range(cantidadPersonas):
    print("---------------------------------------------------------")
    valor = int(input("Ingrese el valor de la entrada del cliente: "))
    edad = int(input("Ingrese la edad del cliente: "))
    print("---------------------------------------------------------")
    if edad < 5:
        print("Usted es menor de 5 años, espere a que crezca")
    elif edad >= 5 and edad <=14:
        descuento = (valor*0.35)/100
        valorFinal =  (valor - descuento)
        print("Usted tiene el 35% de descuento")
        print(f'El total a pagar es: {valorFinal}')
    elif edad >= 15 and edad <=19:
        descuento = (valor*0.25)/100
        valorFinal =  (valor - descuento)
        print("Usted tiene el 25% de descuento")
        print(f'El total a pagar es: {valorFinal}')
    elif edad >= 20 and edad <=45:
        descuento = (valor*0.10)/100
        valorFinal =  (valor - descuento)
        print("Usted tiene el 10% de descuento")
        print(f'El total a pagar es: {valorFinal}')
    elif edad >= 46 and edad <=65:
        descuento = (valor*0.25)/100
        valorFinal =  (valor - descuento)
        print("Usted tiene el 25% de descuento")
        print(f'El total a pagar es: {valorFinal}')
    elif edad >=66:
        descuento = (valor*0.35)/100
        valorFinal =  (valor - descuento)
        print("Usted tiene el 35% de descuento")
        print(f'El total a pagar es: {valorFinal}')