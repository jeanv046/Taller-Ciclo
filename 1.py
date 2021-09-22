


aux = True
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
contador = 0

while(aux):
    placa = int(input("Ingresa el ultimo digito de la placa del automóvil: "))
    contador = contador + 1
    if(placa % 10 == 1 or placa % 10 == 2):
        amarillo = amarillo + 1
    elif(placa % 10 == 3 or placa % 10 == 4):
        rosa = rosa + 1
    elif(placa % 10 == 5 or placa % 10 == 6):
        roja = roja + 1
    elif(placa % 10 == 7 or placa % 10 == 8):
        verde = verde + 1
    elif(placa % 10 == 9 or placa % 10 == 0):
        azul = azul + 1
    fin = input("¿Desea conocer los datos (si o no): ")
    if fin == "si":
        aux = False
        
print(f"La ciudad de Barranquilla ingresaron {contador} automoviles")
print(f"Entran {amarillo} automóviles con calcomanía Amarilla")
print(f"Entran {rosa} automóviles con calcomanía Rosa")
print(f"Entran {roja} automóviles con calcomanía Roja")
print(f"Entran {verde} automóviles con calcomanía Verde")
print(f"Entran {azul} automóviles con calcomanía Azul")

