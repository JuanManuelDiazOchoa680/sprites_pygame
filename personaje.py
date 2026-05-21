# define la clase base Personaje
class Personaje:

    # constructor con nombre y tipo
    def __init__(self):
        # asigna el nombre del personaje
        self.NOMBRE = "nombre por defecto"

        # asigna el tipo del personaje
        self.TIPO = "tipo por defecto"

    # método para que el personaje cante
    def cantar(self):
        ## imprime el mensaje de canto
        print("El personaje llamado " + self.NOMBRE + " canta.")


# define la clase Druida que hereda de Personaje
class Druida(Personaje):
    # constructor de Druida con nombre
    def __init__(self, nombre, nivel):
        self.NOMBRE = nombre
        self.TIPO = "DRUIDA"
        self.NIVEL_DRUIDA = nivel

    # método para inventar una poción
    def inventar_pocion(self):
        # imprime el mensaje de poción
        print("El druida llamado " + self.NOMBRE + " inventa una poción.")


# crear instancia de Druida
pygamix = Druida("Pygamix", 5)

# llamar método cantar
pygamix.cantar()

# llamar método inventar poción
pygamix.inventar_pocion()