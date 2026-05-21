# clase que define un vehículo
class Vehiculo:

    # constructor del vehículo
    def __init__(self, matricula, color, numeroPuertas):
        # guardar matrícula
        self.MATRICULA = matricula
        # guardar color
        self.COLOR = color
        # guardar número de puertas
        self.NUMERO = numeroPuertas
        # guardar estado de funcionamiento
        self.AVANZA = False
        #
        print("Construccion de un vehiculo: " +self.MATRICULA)

    # método para avanzar
    def avanzar(self):
        self.AVANZA = True
        # imprimir avance
        print(self.MATRICULA + " avanza.")

    # método para detenerse
    def detenerse(self):
        self.AVANZA = False
        # imprimir detención
        print(self.MATRICULA + " se detiene.")


# crear instancia de Vehiculo
vehiculo1 = Vehiculo("AR123", "rojo", 3)

vehiculo2 = Vehiculo("FR456", "verde", 5)

# llamar método avanzar
vehiculo1.avanzar()

# llamar método detenerse
vehiculo2.detenerse()
