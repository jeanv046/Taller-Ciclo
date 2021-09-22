vendedores = int(input("cuantos vendedores se van a premiar: "))
comision = 0

for x in range(vendedores):
    nombre = input("Nombre del vendedor: ")
    valorventas = int(input(f"Ingrese el total de ventas de {nombre}: $"))

    if(valorventas <= 20000000):
        comision += valorventas * 0.10
        print(f"la comision de {nombre} vendedor es de {comision}")

    elif(valorventas > 20000000 and valorventas < 40000000):
        comision += valorventas * 0.15
        print(f"la comision del {nombre} es de {comision}")

    elif(valorventas >= 40000000 and valorventas < 80000000):
        comision += valorventas * 0.20
        print(f"la comision del {nombre} es de {comision}")

    elif(valorventas >= 80000000 and valorventas < 160000000):
        comision += valorventas * 0.25
        print(f"la comision del {nombre} es de {comision}")

    elif(valorventas >= 160000000):
        comision += valorventas * 0.30
        print(f"la comision del {nombre} es de {comision}")

    else:
        print("el vendedor no tiene comisione y lo despiden")