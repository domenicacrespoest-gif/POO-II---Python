#declracion de funciones

def saludar():
    print("Hola Dome")
saludar()


#funcion con parametros

def calcular_edad(anio_nacimiento, anio_actual):
    print("La edad es:", anio_actual-anio_nacimiento)
calcular_edad(2006,2026)  

a= int(input("Ingrese su año de nacimiento"))
b=int(input("Ingrese el año actual:")) 
calcular_edad(a,b)


#funciones con retorno

def calcular_iva(precio,iva):
    return precio*iva

resultado=calcular_iva(10,0.15)
print("El iva es", resultado)


#funciones con valores por defecto
def calcular_iva(precio, iva=0.15):
    return precio*iva
resultado=calcular_iva(100)
print("El iva es":, reusltado)

resultado=calcular_iva(100,0.14)
print("El iva es:", resultado)


#Funciones con listas 

def calcular_par(numeros):
    for e in numeros:
        if e%2==0:
            print(f"el numero(e) es par")

        else:
           print(f"El numero (e) es impar")

lista_numeros=range  (0,10, 2)
calcular_par(lista_numeros)

lista_numeros= range (5,0,-1)
for e in lista_numeros:
  print(("e, end (" ")"))

#funciones con tuplas

def suma_numeros(*a):
    return sum(a)

print(suma_numeros(1,2,3))


#diccionarios

def estudiantes(**lista_estudiantes):
    suma_edades=0 
    for nombre,edad in lista_estudiantes.items():
        print("el estudiante", nombre, "tienes",edad,"años")
        suma_edades+= edad
        print("La suma de todas las edades es:" ,suma_edades)
estudiantes(luis=15, anaya=19, miguel=20, dome=20, pepe=23, alan=18, jose=21)

