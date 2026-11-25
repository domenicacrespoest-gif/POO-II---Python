class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        elif cantidad > self.cupos:
            print(f"Error: solo hay {self.cupos} cupos.")
            return False
        else:
            self.cupos -= cantidad
            return True

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<20} {self.precio:<10.2f} {self.cupos:<6}"


# Datos iniciales (dos objetos creados en el programa)
tours = [
    Tour(1, "Centro histórico", 15.00, 20),
    Tour(2, "El Cajas", 35.00, 12)
]

# Menú principal
while True:
    print("\n----- MENU -----")
    print("1. Registrar tour")
    print("2. Mostrar tours")
    print("3. Reservar cupos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del tour: ")
        precio = float(input("Precio: "))
        cupos = int(input("Cupos: "))
        codigo = len(tours) + 1
        nuevo_tour = Tour(codigo, nombre, precio, cupos)
        tours.append(nuevo_tour)
        print(f"Registrado con el código {codigo}.")

    elif opcion == "2":
        print(f"\n{'Código':<8} {'Nombre':<20} {'Precio':<10} {'Cupos':<6}")
        print("-" * 46)
        for tour in tours:
            print(tour)

    elif opcion == "3":
        codigo = int(input("Ingrese el código del tour: "))
        tour_encontrado = None

        for tour in tours:
            if tour.codigo == codigo:
                tour_encontrado = tour
                break

        if tour_encontrado is None:
            print("Error: no existe ese código.")
        else:
            cantidad = int(input("Cantidad de cupos a reservar: "))
            if tour_encontrado.reservar(cantidad):
                print(f"Listo. Quedan {tour_encontrado.cupos} cupos.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")