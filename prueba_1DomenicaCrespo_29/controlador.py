class ControladorTours:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                self._opcion_registrar()
            elif opcion == "2":
                self._opcion_mostrar()
            elif opcion == "3":
                self._opcion_reservar()
            elif opcion == "4":
                self.vista.mostrar_mensaje("Saliendo del programa...")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida")

    def _opcion_registrar(self):
        try:
            nombre, precio_txt, cupos_txt = self.vista.pedir_datos_tour()
            precio = float(precio_txt)
            cupos = int(cupos_txt)
            tour = self.modelo.registrar(nombre, precio, cupos)
            self.vista.mostrar_mensaje(f"Registrado con el código {tour.codigo}.")
        except ValueError as error:
            if "could not convert" in str(error) or "invalid literal" in str(error):
                self.vista.mostrar_mensaje("Error: ingrese valores numéricos válidos.")
            else:
                self.vista.mostrar_mensaje(str(error))

    def _opcion_mostrar(self):
        tours = self.modelo.obtener_tours()
        self.vista.mostrar_tours(tours)

    def _opcion_reservar(self):
        try:
            codigo = int(self.vista.pedir_codigo())
            self.modelo.buscar(codigo)
            cantidad = int(self.vista.pedir_cantidad())
            cupos_restantes = self.modelo.reservar_cupos(codigo, cantidad)
            self.vista.mostrar_mensaje(f"Listo. Quedan {cupos_restantes} cupos.")
        except ValueError as error:
            if "invalid literal" in str(error):
                self.vista.mostrar_mensaje("Error: ingrese un número entero válido.")
            else:
                self.vista.mostrar_mensaje(str(error))