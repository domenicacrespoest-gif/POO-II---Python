class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def validar_reserva(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Error: la cantidad debe ser mayor que cero.")
        if cantidad > self.cupos:
            raise ValueError(f"Error: solo hay {self.cupos} cupos.")

    def reservar(self, cantidad):
        self.validar_reserva(cantidad)
        self.cupos -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<20} {self.precio:<10.2f} {self.cupos:<6}"


class GestorTours:
    def __init__(self):
        self.tours = [
            Tour(1, "Centro histórico", 15.00, 20),
            Tour(2, "El Cajas", 35.00, 12),
        ]

    def registrar(self, nombre, precio, cupos):
        if not nombre or not nombre.strip():
            raise ValueError("Error: el nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("Error: el precio debe ser mayor que cero.")
        if cupos < 0:
            raise ValueError("Error: los cupos no pueden ser negativos.")

        codigo = len(self.tours) + 1
        nuevo_tour = Tour(codigo, nombre.strip(), precio, cupos)
        self.tours.append(nuevo_tour)
        return nuevo_tour

    def buscar(self, codigo):
        for tour in self.tours:
            if tour.codigo == codigo:
                return tour
        raise ValueError("Error: no existe ese código.")

    def reservar_cupos(self, codigo, cantidad):
        tour = self.buscar(codigo)
        tour.reservar(cantidad)
        return tour.cupos

    def obtener_tours(self):
        return self.tours