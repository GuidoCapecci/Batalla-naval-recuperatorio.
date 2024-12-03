
import pygame

# ##### DIMENSIONES DE LA VENTANA PRINCIPAL #####
ANCHO_VENTANA = 980
ALTO_VENTANA = 780
DIMENCIONES_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

# ##### COLORES #####
# Colores básicos
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (20, 20, 150)
GRIS = (150, 150, 150)
TRANSPARENTE = (GRIS, 128)
CREMA = (245, 245, 220)
CHOCOLATE = (139, 69, 19)

# Colores específicos para los barcos
COLOR_AGUA = (20, 20, 100)
COLOR_SUBMARINO = (50, 50, 50)
COLOR_DESTRUCTOR = (128, 0, 128)
COLOR_CRUCERO = (20, 255, 20)
COLOR_ACORAZADO = (0, 80, 0)
BLANCO_MARINERO = (255, 222, 173)
AZUL_MARINERO = (0, 0, 128)

# ##### CONFIGURACIÓN DE BOTONES #####
# Dimensiones de los botones
BOTON_Y = 100  # Coordenada Y de los botones
BOTON_X = 100  # Coordenada X de los botones
BOTON_ANCHO = 200  # Ancho de los botones
BOTON_ALTO = 50  # Alto de los botones

# Posiciones de los botones en el eje Y
POS_Y_NIVEL = 100
POS_Y_JUGAR = 200
POS_Y_PUNTAJES = 300
POS_Y_SALIR = 400

# ##### CONFIGURACIÓN DEL TABLERO #####
# Tamaño de cada celda en el tablero
TAMAÑO_CELDA = 30
