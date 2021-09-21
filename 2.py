
animal = input('Escoja su animal: \n\t*Elefante. \n\t*Jirafa. \n\t*Chimpancés.\n= ')
menor = 0
mediano = 0
grande = 0

if animal == 'elefante' or animal == 'Elefante':
    for x in range(20):
        muestra = int(input(f'Edad del elefante numero {x + 1}: '))
        if muestra >= 0 and muestra <= 1:
            menor = menor + 1
        elif muestra > 1 and muestra < 3:
            mediano = mediano + 1
        elif muestra > 3:
            grande = grande + 1
    resul1 = (menor / 20)* 100
    resul2 = (mediano / 20)* 100
    resul3 = (grande / 20)* 100
    print(f'El porcentaje de los {animal}: \n 0 - 1 años: {resul1}% \n 2 años: {resul2}% \n 3 o mas años: {resul3}%')
elif animal == 'jirafas' or animal == 'Jirafas':
    for x in range(15):
        muestra = int(input(f'Edad de la {animal} numero {x + 1}: '))
        if muestra >= 0 and muestra <= 1:
            menor = menor + 1
        elif muestra > 1 and muestra < 3:
            mediano = mediano + 1
        elif muestra > 3:
            grande = grande + 1
    resul1 = (menor / 15)* 100
    resul2 = (mediano / 15)* 100
    resul3 = (grande / 15)* 100
    print(f'El porcentaje de las {animal}: \n 0 - 1 años: {resul1}% \n 2 años: {resul2}% \n 3 o mas años: {resul3}%')
elif animal == 'chimpances' or animal == 'Chimpances' or animal == 'Chimpancés':
    for x in range(40):
        muestra = int(input(f'Edad del {animal} numero {x + 1}: '))
        if muestra >= 0 and muestra <= 1:
            menor = menor + 1
        elif muestra > 1 and muestra < 3:
            mediano = mediano + 1
        elif muestra > 3:
            grande = grande + 1
    resul1 = (menor / 40)* 100
    resul2 = (mediano / 40)* 100
    resul3 = (grande / 40)* 100
    print(f'El porcentaje de los {animal}: \n 0 - 1 años: {resul1}% \n 2 años: {resul2}% \n 3 o mas años: {resul3}%')
else:
    print('Ingresa correctamente un animal. ')