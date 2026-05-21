# importar pygame para usar sprites y ventanas
import pygame

# inicializar todos los módulos de pygame
pygame.init()


# color rojo del cuadrado
COLOR_ROJO=(255,0,0)
# color azul del fondo
COLOR_AZUL=(0,0,255)

# clase que define el sprite del cuadrado
class CUADRADO(pygame.sprite.Sprite):
    # constructor del sprite
    def __init__(self):
        # inicializar la clase base Sprite
        pygame.sprite.Sprite.__init__(self)

        # crear superficie del cuadrado
        self.image=pygame.Surface((80,80))

        # pintar el cuadrado de rojo
        self.image.fill(COLOR_ROJO)

        # obtener el rectángulo para posicionar el sprite
        self.rect=self.image.get_rect()

        # establecer posición horizontal inicial
        self.rect.x=200

        # establecer posición vertical inicial
        self.rect.y=200

        # velocidad horizontal del cuadrado
        self.DESPLAZAMIENTO=3

    # actualizar la posición del cuadrado
    def update(self):
        # mover el cuadrado en el eje x
        self.rect.x+=self.DESPLAZAMIENTO

        # si llega al borde derecho
        if self.rect.x >= 320:
            # fijar posición en el borde derecho
            self.rect.x = 320

            # invertir dirección al chocar
            self.DESPLAZAMIENTO = -3

        # si llega al borde izquierdo
        elif self.rect.x <= 0:
            # fijar posición en el borde izquierdo
            self.rect.x = 0

            # invertir dirección al chocar
            self.DESPLAZAMIENTO = 3


# crear la ventana del juego
screen=pygame.display.set_mode((400,400))

# crear la superficie de fondo del mismo tamaño
background=pygame.Surface(screen.get_size())

# pintar el fondo de azul
background.fill(COLOR_AZUL)

# crear un grupo para manejar sprites
all_sprites = pygame.sprite.Group()

# crear el sprite del cuadrado
cuadrado = CUADRADO()

# añadir el cuadrado al grupo de sprites
all_sprites.add(cuadrado)

# crear reloj para controlar FPS
clock=pygame.time.Clock()

# bandera para mantener el juego en ejecución
running=True

# bucle principal del juego
while running:
    # recorrer todos los eventos recibidos
    for event in pygame.event.get():
        # cerrar el juego si se solicita
        if event.type == pygame.QUIT: 
            running=False
    # limpiar la pantalla usando el fondo
    all_sprites.clear(screen,background)

    # actualizar todos los sprites del grupo
    all_sprites.update()

    # dibujar todos los sprites en pantalla
    all_sprites.draw(screen)

    # actualizar la pantalla visible
    pygame.display.flip()
    # mantener 60 cuadros por segundo
    clock.tick(60)
# cerrar pygame al salir del bucle
pygame.quit()


# VIVA AVERNUS
