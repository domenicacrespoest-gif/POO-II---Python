def menu_principal():
    print("\n//// MENU PRINCIPAL////")
    print("1.INGRESE SU NOMBRE")
    print("2.PREGUNTAS")
    print("3.SALIR")

def saludo ():
    nombre=input("Ingrese su nombre:") 
    print(f"HOLA bienvenid@ {nombre} a un programa en donde se ejecutaran diferentes preguntas acerca de la leccion2")   

def sub_menu():
    print("\n ----MENU PREGUNTAS----")
    print("1. EJERCICIO 1")
    print("2. EJERCICIO 2")
    print("3. EJERCICIO 3")
    print("4. EJERCICIO 4")
    print("5. EJERCICIO 5")
    print("6. EJERCICIO 6")
    print("7. EJERCICIO 7")
    print("8. EJERCICIO 8")
    print("9. EJERCICIO 9")
    print("10. EJERCICIO 10")
    print("11. EJERCICIO 11")
    print("12. REGRESAR AL MENU PRINCIPAL")

def ejercicio_1():
    print("""\n1: ¿Qué imprime el siguiente código?
socio = {"nombre": "Ana", "saldo": 120}
print(socio.get("correo", "Sin correo"))""")
    print("Respuesta:")
    socio = {"nombre": "Ana", "saldo": 120}
    print(socio.get("correo", "Sin correo"))

def ejercicio_2():
    print("""\n 2: ¿Qué imprime el siguiente código?
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(len(a & b))""")
    print("Respuesta:")
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    print(len(a & b))

def ejercicio_3():
    print("""\n 3: ¿Qué imprime el siguiente código?
print(type(10.0))""")
    print("Respuesta:")
    print(type(10.0))

def ejercicio_4():
    print("""\n4: ¿Qué imprime el siguiente código?
texto = "TEC Azuay"
print(texto[4:7])""")
    print("Respuesta:")
    texto = "TEC Azuay"
    print(texto[4:7])

def ejercicio_5():
    print("""\n5: ¿Qué imprime el siguiente código?
print("ab" * 3)""")
    print("Respuesta:")
    print("ab" * 3)

def ejercicio_6():
    print("""\n 6: ¿Cuántas veces se imprime «*» en el siguiente código?
for i in range(3):
    for j in range(2):
        print("*", end="")""")
    print("Respuesta:")
    for i in range(3):
        for j in range(2):
            print("*", end="")
    print(" -> Se imprime 6 veces")

def ejercicio_7():
    print("""\n 7: ¿Qué imprime el siguiente código?
for i in range(3, 0, -1):
    print(i, end=" ")""")
    print("Respuesta:")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print()

def ejercicio_8():
    print("""\n 8: ¿Qué imprime el siguiente código?
saldo = 350
if saldo >= 1000:
    print("Oro")
elif saldo >= 100:
    print("Plata")
else:
    print("Básica")""")
    print("Respuesta:")
    saldo = 350
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")

def ejercicio_9():
    print("""\n 9: ¿Qué imprime el siguiente código?
notas = {"Ana": 10, "Luis": 8}
for nombre, nota in notas.items():
    print(f"{nombre}:{nota}", end=" ")""")
    print("Respuesta:")
    notas = {"Ana": 10, "Luis": 8}
    for nombre, nota in notas.items():
        print(f"{nombre}:{nota}", end=" ")
    print()

def ejercicio_10():
    print("""\n 10: ¿Qué imprime el siguiente código?
for i in range(1, 10, 3):
    print(i, end=" ")""")
    print("Respuesta:")
    for i in range(1, 10, 3):
        print(i, end=" ")
    print()

def ejercicio_11():
    print("""\n 11: Ejercicio 9. Pares e impares
Pida números enteros con input() hasta que el usuario escriba fin. 
Guárdelos en una lista y luego, con comprensiones, cree una lista de pares y otra de impares. 
Muestre ambas listas, ordenadas, y la suma de cada una.""")

    print("\nRespuesta (Ejecución):")
    numeros = []

    while True:
        entrada = input("Ingrese un número entero (o colocar 'fin'): ")
        if entrada.lower() == "fin":
            break
        numeros.append(int(entrada))

    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    pares.sort()
    impares.sort()

    print(f"Los números pares ordenados son: {pares} | Suma: {sum(pares)}")
    print(f"Los números impares ordenados son: {impares} | Suma: {sum(impares)}")
while True:
    menu_principal()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        saludo()

    elif opcion == "2":
        while True:
            sub_menu()
            sub = input("Elige una opción (1-12): ")

            if sub == "1":
                ejercicio_1()
            elif sub == "2":
                ejercicio_2()
            elif sub == "3":
                ejercicio_3()
            elif sub == "4":
                ejercicio_4()
            elif sub == "5":
                ejercicio_5()
            elif sub == "6":
                ejercicio_6()
            elif sub == "7":
                ejercicio_7()
            elif sub == "8":
                ejercicio_8()
            elif sub == "9":
                ejercicio_9()
            elif sub == "10":
                ejercicio_10()
            elif sub == "11":
                ejercicio_11()
            elif sub == "12":
                print("\nRegresando al menú principal...")
                break
            else:
                print("\nOpción no válida. Ingresa un número del 1 al 12.")

    elif opcion == "3":
        print("\nSaliendo del programa... ¡Gracias!")
        break

    else:
        print("\nOpción no válida. Elija 1, 2 o 3.")







