
obreros  = int(input('Cuantos trabajadores laboran en la empresa: '))

for x in range(obreros):
    horas = int(input('Cuantas horas trabajo a la semana: '))
    if horas > 0 and horas <= 40:
        total = horas * 20
        print(f'Su salario semanal es de: {total}')
    elif horas > 40:
        horasextras = horas - 40
        total = (horasextras * 25)+(40 * 20)
        print(f'Su salario semanal es {total}')
    