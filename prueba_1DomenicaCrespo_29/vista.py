class VistaTours:
    def mostrar_menu(self):
        print("\n----- MENU -----")
        print("1. Registrar tour")
        print("2. Mostrar tours")
        print("3. Reservar cupos")
        print("4. Salir")
        return input("Seleccione una opción: ")

    def pedir_datos_tour(self):
        nombre = input("Nombre del tour: ")
        precio = input("Precio: ")
        cupos = input("Cupos: ")
        return nombre, precio, cupos

    def pedir_codigo(self):
        return input("Ingrese el código del tour: ")

    def pedir_cantidad(self):
        return input("Cantidad de cupos a reservar: ")

    def mostrar_tours(self, tours):
        print(f"\n{'Código':<8} {'Nombre':<20} {'Precio':<10} {'Cupos':<6}")
        print("-" * 46)
        for tour in tours:
            print(tour)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)