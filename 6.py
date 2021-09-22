
pesoantiguo = []
for x in range(5):
    pesoant = float(input(f'Cual fue tu peso persona #{x +1}: '))
    pesoantiguo.append(pesoant)

pesopromedio = []
for persona in range(5):
    suma = 0
    for medida in range(10):
        peso = float(input(f'Digita tu peso persona #{persona + 1}: '))
        suma = suma + peso
    promedio = suma / 10
    pesopromedio.append(promedio)

for pesoindice in range(5):
    if pesoantiguo[pesoindice] > pesopromedio[pesoindice]:
        pesototal = pesoantiguo[pesoindice] - pesopromedio[pesoindice]
        print(f"Bajaste de peso {pesototal} klg")
    elif pesoantiguo[pesoindice] < pesopromedio[pesoindice]:
        pesototal = pesoantiguo[pesoindice] - pesopromedio[pesoindice]
        if pesototal < 0:
            pesototal = pesototal * - 1
            print(f'Subiste de peso {pesototal} klg')
    

    


    