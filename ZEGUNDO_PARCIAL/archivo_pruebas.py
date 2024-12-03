
# import pygame



# ############################################################################################################################
# """#########################################################################################################################
# ############################################################################################################################
# """#########################################################################################################################
# ############################################################################################################################
# """#########################################################################################################################
# ############################################################################################################################
# """#########################################################################################################################



# #Dimenciones ventana principal.
# ANCHO_VENTANA = 980
# ALTO_VENTANA = 780
# DIMENCIONES_VENTANA = (ANCHO_VENTANA,ALTO_VENTANA)



# #Colores:
# BLANCO=(255,255,255)
# NEGRO =(0,0,0)
# ROJO =(255,0,0)
# VERDE =(0,255,0)
# AZUL =(0,0,255)
# AZUL_CLARO =(20,20,150)
# GRIS = (150,150,150)
# # TRANSPARENTE = pygame.SRCALPHA #
# TRANSPARENTE = (GRIS,128)
# CREMA = (245, 245, 220)

# CHOCOLATE = (139, 69, 19)

# #Navios
# COLOR_AGUA = (20,20,100)

# COLOR_SUBMARINO = (50,50,50)
# COLOR_DESTRUCTOR = (128,0,128)
# COLOR_CRUCERO = (20,255,20)
# COLOR_ACORAZADO = (0,80,0)
# BLANCO_MARINERO = (255, 222, 173)
# AZUL_MARINERO = (0, 0, 128)

# #Botones:
# BOTON_Y = 100 #coordenada Y de los botones
# BOTON_X = 100  #coordenada X de los botones
# BOTON_ANCHO = 200  #ancho botones
# BOTON_ALTO = 50  #alto botones

# POS_Y_NIVEL = 100
# POS_Y_JUGAR = 200
# POS_Y_PUNTAJES = 300
# POS_Y_SALIR = 400


# #Tablero

# # ANCHO_CUADRADOS = 25
# # ALTO_CUADRADOS = 25
# # DIMENCION_CUADRADOS = (ANCHO_CUADRADOS,ALTO_CUADRADOS)

# TAMAÑO_CELDA=30

# [{'fila': 5, 'columna': 4, 'valor': 1, 'tocado': False}]
# [{'fila': 0, 'columna': 9, 'valor': 1, 'tocado': False}]
# [{'fila': 7, 'columna': 9, 'valor': 1, 'tocado': False}]
# [{'fila': 5, 'columna': 6, 'valor': 1, 'tocado': False}]

# [{'fila': 0, 'columna': 5, 'valor': 2, 'tocado': False}, {'fila': 0, 'columna': 6, 'valor': 2, 'tocado': False}]
# [{'fila': 6, 'columna': 1, 'valor': 2, 'tocado': False}, {'fila': 7, 'columna': 1, 'valor': 2, 'tocado': False}]
# [{'fila': 4, 'columna': 3, 'valor': 2, 'tocado': False}, {'fila': 5, 'columna': 3, 'valor': 2, 'tocado': False}]

# [{'fila': 0, 'columna': 1, 'valor': 3, 'tocado': False}, {'fila': 1, 'columna': 1, 'valor': 3, 'tocado': False}, {'fila': 2, 'columna': 1, 'valor': 3, 'tocado': False}]
# [{'fila': 2, 'columna': 2, 'valor': 3, 'tocado': False}, {'fila': 2, 'columna': 3, 'valor': 3, 'tocado': False}, {'fila': 2, 'columna': 4, 'valor': 3, 'tocado': False}]

# [{'fila': 2, 'columna': 6, 'valor': 4, 'tocado': False}, {'fila': 2, 'columna': 7, 'valor': 4, 'tocado': False}, {'fila': 2, 'columna': 8, 'valor': 4, 'tocado': False}, {'fila': 2, 'columna': 9, 'valor': 4, 'tocado': False}]





# barcos_prueba=[

# [    
# [{'fila': 3, 'columna': 8, 'valor': 1}],
# [{'fila': 6, 'columna': 1, 'valor': 1}],
# [{'fila': 3, 'columna': 9, 'valor': 1}],
# [{'fila': 7, 'columna': 5, 'valor': 1}],
# ],

# [
# [{'fila': 4, 'columna': 5, 'valor': 2}, {'fila': 4, 'columna': 6, 'valor': 2}],
# [{'fila': 8, 'columna': 2, 'valor': 2}, {'fila': 9, 'columna': 2, 'valor': 2}],
# [{'fila': 2, 'columna': 2, 'valor': 2}, {'fila': 2, 'columna': 3, 'valor': 2}],
# ],


# [
# [{'fila': 7, 'columna': 7, 'valor': 3}, {'fila': 7, 'columna': 8, 'valor': 3}, {'fila': 7, 'columna': 9, 'valor': 3}],
# [{'fila': 4, 'columna': 2, 'valor': 3}, {'fila': 5, 'columna': 2, 'valor': 3}, {'fila': 6, 'columna': 2, 'valor': 3}],
# ],

# [
# [{'fila': 3, 'columna': 4, 'valor': 4}, {'fila': 3, 'columna': 5, 'valor': 4}, {'fila': 3, 'columna': 6, 'valor': 4}, {'fila': 3, 'columna': 7, 'valor': 4}]
# ]

# ]


# for i in range(len(barcos_prueba)):
#     for j in range(len(barcos_prueba[i])):
#         for k in range(len(barcos_prueba[i][j])):
#             print(barcos_prueba[i][j][k]['fila'])



# [
# [

# [{'fila': 3, 'columna': 4, 'valor': 1, 'tocado': False}],
# [{'fila': 2, 'columna': 5, 'valor': 1, 'tocado': False}],
# [{'fila': 7, 'columna': 3, 'valor': 1, 'tocado': False}],
# [{'fila': 2, 'columna': 4, 'valor': 1, 'tocado': False}]],
# [[{'fila': 4, 'columna': 4, 'valor': 2, 'tocado': False},
# {'fila': 5, 'columna': 4, 'valor': 2, 'tocado': False}],
# [{'fila': 7, 'columna': 6, 'valor': 2, 'tocado': False},
# {'fila': 7, 'columna': 7, 'valor': 2, 'tocado': False}],
# [{'fila': 3, 'columna': 1, 'valor': 2, 'tocado': False},
# {'fila': 3, 'columna': 2, 'valor': 2, 'tocado': False}]],
# [[{'fila': 7, 'columna': 5, 'valor': 3, 'tocado': False},
# {'fila': 8, 'columna': 5, 'valor': 3, 'tocado': False},
# {'fila': 9, 'columna': 5, 'valor': 3, 'tocado': False}],
# [{'fila': 2, 'columna': 6, 'valor': 3, 'tocado': False},
# {'fila': 3, 'columna': 6, 'valor': 3, 'tocado': False},
# {'fila': 4, 'columna': 6, 'valor': 3, 'tocado': False}]],
# [[{'fila': 0, 'columna': 0, 'valor': 4, 'tocado': False},
# {'fila': 1, 'columna': 0, 'valor': 4, 'tocado': False},
# {'fila': 2, 'columna': 0, 'valor': 4, 'tocado': False},
# {'fila': 3, 'columna': 0, 'valor': 4, 'tocado': False}]
# ]
# ]



# [{'fila': 5, 'columna': 4, 'valor': 1, 'tocado': False}]
# [{'fila': 0, 'columna': 9, 'valor': 1, 'tocado': False}]
# [{'fila': 7, 'columna': 9, 'valor': 1, 'tocado': False}]
# [{'fila': 5, 'columna': 6, 'valor': 1, 'tocado': False}]

# [{'fila': 0, 'columna': 5, 'valor': 2, 'tocado': False}, {'fila': 0, 'columna': 6, 'valor': 2, 'tocado': False}]
# [{'fila': 6, 'columna': 1, 'valor': 2, 'tocado': False}, {'fila': 7, 'columna': 1, 'valor': 2, 'tocado': False}]
# [{'fila': 4, 'columna': 3, 'valor': 2, 'tocado': False}, {'fila': 5, 'columna': 3, 'valor': 2, 'tocado': False}]

# [{'fila': 0, 'columna': 1, 'valor': 3, 'tocado': False}, {'fila': 1, 'columna': 1, 'valor': 3, 'tocado': False}, {'fila': 2, 'columna': 1, 'valor': 3, 'tocado': False}]
# [{'fila': 2, 'columna': 2, 'valor': 3, 'tocado': False}, {'fila': 2, 'columna': 3, 'valor': 3, 'tocado': False}, {'fila': 2, 'columna': 4, 'valor': 3, 'tocado': False}]

# [{'fila': 2, 'columna': 6, 'valor': 4, 'tocado': False}, {'fila': 2, 'columna': 7, 'valor': 4, 'tocado': False}, {'fila': 2, 'columna': 8, 'valor': 4, 'tocado': False}, {'fila': 2, 'columna': 9, 'valor': 4, 'tocado': False}]


# # import pygame.mixer as mixer
# # pygame.mixer.init()
# # mixer.music.play()
# # mixer.music.load("assets\\sounds\\musica_fondo.mp3")
# # ruido_bala = mixer.Sound("assets\\sounds\\Efecto_disparo.mp3")
# # ruido_bala.set_volume(0.3)
# # mixer.music.set_volume(10)
        

#             # if event.type == pygame.MOUSEBUTTONDOWN:
#             #     ruido_bala.play()