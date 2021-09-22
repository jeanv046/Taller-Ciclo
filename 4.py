
datos = int(input('seleccione la opcion: \n  1.Hombres  \n  2.Mujeres  \n  3.Grupo de alumnos \n= '))

if datos == 1: 
    cantidadhombres = int(input('Cuantos hombres va a ingresar: '))
    for x in range(cantidadhombres):
        edad = int(input('Que edad tienes: '))
        suma = suma + edad
    promhombres = (suma / cantidadhombres) * 100
    print(f'El promedio de edad en los hombres es de {promhombres}%')
elif datos == 2: 
    cantidadmujeres = int(input('Cuantas mujeres va a ingresar: '))
    for x in range(cantidadmujeres):
        edad = int(input('Que edad tienes: '))
        suma = suma + edad
    promujeres = (suma / cantidadmujeres) * 100
    print(f'El promedio de edad en los hombres es de {promujeres}%')    
elif datos == 3: 
    cantidadgrupo = int(input('Cuantos alumnos va a ingresar: '))
    for x in range(cantidadgrupo):
        edad = int(input('Que edad tienes: '))
        suma = suma + edad
    promgrupo = (suma / cantidadgrupo) * 100
    print(f'El promedio de edad en los hombres es de {promgrupo}%')
else:
    print('Digita un numero del 1 - 3.')