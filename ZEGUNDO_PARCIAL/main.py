import pygame
from funciones import *
from configuraciones import *


pygame.init()
pygame.mixer.init()


#ICONO
imagen_logo = pygame.image.load("ZEGUNDO_PARCIAL/archivos/imagen_brujula.webp")
pygame.display.set_icon(imagen_logo)
#TITULO
pygame.display.set_caption("Batalla Naval UTN")
#VENTANA
ventana_principal = pygame.display.set_mode((DIMENCIONES_VENTANA))

#IMAGENES:

#INICIO:
imagen_inicio = pygame.image.load("ZEGUNDO_PARCIAL/archivos/fondo_barco.jpg")
imagen_inicio = pygame.transform.scale(imagen_inicio, DIMENCIONES_VENTANA)
#FONDO TABLERO
imagen_fondo_tablero = pygame.image.load("ZEGUNDO_PARCIAL/archivos/imagen_fondo_tablero.webp")
imagen_fondo_tablero = pygame.transform.scale(imagen_fondo_tablero, DIMENCIONES_VENTANA)
#FONDO PUNTAJES
imagen_fondo_puntajes = pygame.image.load("ZEGUNDO_PARCIAL/archivos/saludo_militar.jpg")
imagen_fondo_puntajes = pygame.transform.scale(imagen_fondo_puntajes, DIMENCIONES_VENTANA)
#FONDO NIVLES
imagen_fondo_niveles = pygame.image.load("ZEGUNDO_PARCIAL/archivos/timon.jpg")
imagen_fondo_niveles = pygame.transform.scale(imagen_fondo_niveles, DIMENCIONES_VENTANA)

##########################################################################################################
#SONIDOS
##########################################################################################################
#Fondo:
pygame.mixer.music.load("ZEGUNDO_PARCIAL/archivos/Age of Mythology Soundtrack - 09 Adult Swim (online-audio-converter.com).ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1, start=0.0)

#Efectos:
efecto_agua = pygame.mixer.Sound("ZEGUNDO_PARCIAL/archivos/agua (online-audio-converter.com).ogg")
efecto_agua.set_volume(0.3)

efecto_cañon = pygame.mixer.Sound("ZEGUNDO_PARCIAL/archivos\cañon (online-audio-converter.com).ogg")
efecto_cañon.set_volume(0.3)

efecto_victoria = pygame.mixer.Sound("ZEGUNDO_PARCIAL/archivos/victoria (online-audio-converter.com).ogg")
efecto_victoria.set_volume(0.3)


##########################################################################################################
# FUNCIONES
##########################################################################################################

#Mostrar top 5

def mostrar_top_5(lista: list)->None:
    """
    Ordena una lista de puntajes de manera descendente y los muestra en pantalla.
    Parámetros:
    lista (list): Lista de enteros que representan los puntajes a mostrar.
    Retorna:
    None
    """

    lista_ordenada = ordenar_lista(lista,"DESC")

    fuente = pygame.font.SysFont("consola", 60)

    eje_x = (centrar_eje_x(ANCHO_VENTANA,BOTON_ANCHO))
    eje_y = 400

    lista_top_5 = [lista_ordenada[0],lista_ordenada[1],lista_ordenada[2],lista_ordenada[3],lista_ordenada[4]]
    contador = 0

    for i in range(len(lista_top_5)):
        contador += 1
        puntaje = lista_ordenada[i]
        texto = fuente.render((f"{contador}-{puntaje:04d}"),True,CREMA,AZUL_MARINERO)

        ventana_principal.blit(texto,(eje_x,eje_y))

        eje_y += BOTON_ALTO


# Puntos: {puntos:04d}
#BIBUJAR TABLERO

def dibujar_tablero(matriz)->list:
    """
    Dibuja el tablero de juego en pantalla utilizando rectángulos de colores
    para representar las celdas del campo de batalla.
    Parámetros:
    matriz (list): Matriz que representa el estado del campo de batalla.
    Retorna:
    list: Lista de rectángulos que corresponden a cada celda de la matriz.
    """

    filas = len(matriz)
    columnas = len(matriz[0])

    matriz_rectangulos = crear_matriz(dificultad,None)

    # Esto quizas haya que convertirlo en funcion
    if len(matriz) == 10:
        tamaño_celda = 40
    elif len(matriz) == 20:
        tamaño_celda = 30
    else:
        tamaño_celda = 15

    #Esto hay que convertirlo en funcion:
    #Centrar eje_X
    ancho_matriz = tamaño_celda * len(matriz[0])
    ancho_matriz_mitad = ancho_matriz // 2
    eje_x_centrado = (ANCHO_VENTANA // 2) - ancho_matriz_mitad
    #Centrar eje_y
    alto_matriz = tamaño_celda * len(matriz)
    alto_matriz_mitad = alto_matriz // 2
    eje_y_centrado = (ALTO_VENTANA // 2) - alto_matriz_mitad

    for i in range(len(matriz)):
        
        for j in range(len(matriz[0])):

            eje_x = j*tamaño_celda
            eje_y = i*tamaño_celda

            rectangulo = pygame.Rect(eje_x_centrado + eje_x, eje_y_centrado + eje_y, tamaño_celda, tamaño_celda)
            
            matriz_rectangulos[i][j] = rectangulo

            valor = matriz[i][j]

            match valor:
                case 0:
                    color = COLOR_AGUA
                case 1:
                    color = COLOR_SUBMARINO
                case 2:
                    color = COLOR_DESTRUCTOR
                case 3:
                    color = COLOR_CRUCERO
                case 4:
                    color = COLOR_ACORAZADO


            pygame.draw.rect(ventana_principal, color, rectangulo)    #se le puede pasar como coordenada y dimencion un rectangulo 

    return matriz_rectangulos

# CREAR BOTONES

def crear_botones_tablero(matriz_rectangulos, matriz_estado_celdas)->None:
    """
    Genera botones en el tablero, con rectángulos grises y bordes negros,
    basados en el estado de cada celda.
    Parámetros:
    matriz_rectangulos (list): Lista de rectángulos que representan las celdas del tablero.
    matriz_estado_celdas (list): Matriz de valores booleanos que indica el estado de cada celda.
    Retorna:
    None
    """

    # ocultador = 0
    for i in range(len(matriz_rectangulos)):
        for j in range(len(matriz_rectangulos[0])):
            rectangulo = matriz_rectangulos[i][j]
            estado_ocultador = matriz_estado_celdas[i][j]

            if estado_ocultador == True:
                ocultador = 2
            else:
                ocultador = 0
            
            pygame.draw.rect(ventana_principal, GRIS, rectangulo, width=ocultador)
            pygame.draw.rect(ventana_principal, NEGRO, rectangulo,width=2)


#MENU INICIO:

#################################################################################################################
#PANTALLA 1 (MENU)
#################################################################################################################
#Botones:

boton_x_centrado = centrar_eje_x(ANCHO_VENTANA,BOTON_ANCHO)

pos_nivel=(boton_x_centrado,50)
pos_jugar=(boton_x_centrado,110)
pos_puntaje=(boton_x_centrado,170)
pos_sonido=(boton_x_centrado,230)
pos_salir=(boton_x_centrado,290)

rectangulo_nivel = pygame.Rect(pos_nivel[0],pos_nivel[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_jugar = pygame.Rect(pos_jugar[0],pos_jugar[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_puntaje = pygame.Rect(pos_puntaje[0],pos_puntaje[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_sonido = pygame.Rect(pos_sonido[0],pos_sonido[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_salir = pygame.Rect(pos_salir[0],pos_salir[1],BOTON_ANCHO,BOTON_ALTO,)

#Textos:
fuente_botones = pygame.font.SysFont("consola", 45)

texto_nivel = fuente_botones.render("Nivel", True, NEGRO,None)
texto_jugar = fuente_botones.render("Jugar", True, NEGRO,None)
texto_puntaje = fuente_botones.render("Puntaje", True, NEGRO,None)
texto_sonido = fuente_botones.render("Sonido", True, NEGRO,None)
texto_salir = fuente_botones.render("Salir", True, NEGRO,None)

#Dimenciones para centrar

dimension_texto_nivel = texto_nivel.get_size()
dimension_texto_jugar = texto_jugar.get_size()
dimension_texto_puntaje = texto_puntaje.get_size()
dimension_texto_sonido = texto_sonido.get_size()
dimension_texto_salir = texto_salir.get_size()


# Centrar los textos en los botones
coordenadas_texto_nivel = centrar_objetos_2(rectangulo_nivel.size, texto_nivel.get_size(), pos_nivel) # (tambien podria ser (reactangulo.width reactangulo.height))
coordenadas_texto_jugar = centrar_objetos_2(rectangulo_jugar.size, texto_jugar.get_size(), pos_jugar)
coordenadas_texto_puntaje = centrar_objetos_2(rectangulo_puntaje.size, texto_puntaje.get_size(), pos_puntaje)
coordenadas_texto_sonido = centrar_objetos_2(rectangulo_sonido.size, texto_sonido.get_size(), pos_sonido)
coordenadas_texto_salir = centrar_objetos_2(rectangulo_salir.size, texto_salir.get_size(), pos_salir)

######################################################################################################################
# BOTON DE VOLVER PANTALLA 2 3 Y 4
######################################################################################################################
pos_volver = [10,10]

rectangulo_volver = pygame.Rect(pos_volver[0], pos_volver[1],BOTON_ANCHO,BOTON_ALTO,)
fuente_volver = pygame.font.SysFont("consola", 45)
texto_volver = fuente_volver.render("Volver", True, NEGRO,None)
dimension_texto_volver = texto_volver.get_size()
coordenadas_texto_volver = centrar_objetos_2(rectangulo_volver.size, texto_volver.get_size(), pos_volver)

######################################################################################################################
#PANTALLA 2 (JUEGO)
######################################################################################################################

#Reiniciar
pos_reiniciar = [pos_volver[0]+BOTON_ANCHO+10,10]

rectangulo_reiniciar = pygame.Rect(pos_reiniciar[0], pos_reiniciar[1],BOTON_ANCHO,BOTON_ALTO,)
fuente_reiniciar = pygame.font.SysFont("consola", 45)
texto_reiniciar = fuente_reiniciar.render("Reiniciar", True, NEGRO,None)
dimension_texto_reiniciar = texto_reiniciar.get_size()
coordenadas_texto_reiniciar = centrar_objetos_2(rectangulo_reiniciar.size, texto_reiniciar.get_size(), pos_reiniciar)

#PUNTOS
puntos = 0000
pos_puntos = [ANCHO_VENTANA - BOTON_ANCHO + 10, pos_volver[1]]

rectangulo_puntos = pygame.Rect(pos_puntos[0], pos_puntos[1],BOTON_ANCHO,BOTON_ALTO,)
fuente_puntos = pygame.font.SysFont("consola", 45)

#########################################################################################################################
#PANTALLA 3 (nivel)
#########################################################################################################################
#Botones:

boton_x_centrado = centrar_eje_x(ANCHO_VENTANA,BOTON_ANCHO)

pos_facil=(boton_x_centrado,50)
pos_medio=(boton_x_centrado,110)
pos_dificil=(boton_x_centrado,170)

rectangulo_facil = pygame.Rect(pos_facil[0],pos_facil[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_medio = pygame.Rect(pos_medio[0],pos_medio[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_dificil = pygame.Rect(pos_dificil[0],pos_dificil[1],BOTON_ANCHO,BOTON_ALTO,)

#Textos:

fuente_botones = pygame.font.SysFont("consola", 45)

texto_facil = fuente_botones.render("Facil", True, CREMA,None)
texto_medio = fuente_botones.render("Medio", True, CREMA,None)
texto_dificil = fuente_botones.render("Dificil", True, CREMA,None)

#Dimenciones para centrar

dimension_texto_facil = texto_facil.get_size()
dimension_texto_medio = texto_medio.get_size()
dimension_texto_dificil = texto_dificil.get_size()

# Centrar los textos en los botones
coordenadas_texto_facil = centrar_objetos_2(rectangulo_facil.size, texto_facil.get_size(), pos_facil) # (tambien podria ser (reactangulo.width reactangulo.height))
coordenadas_texto_medio = centrar_objetos_2(rectangulo_medio.size, texto_medio.get_size(), pos_medio)
coordenadas_texto_dificil = centrar_objetos_2(rectangulo_dificil.size, texto_dificil.get_size(), pos_dificil)

#########################################################################################################################
#PANTALLA 4 (puntajes)
#########################################################################################################################

###########################################################################################################################
# EJECUCION
###########################################################################################################################
"""para inicializar el juego en 10"""
dificultad = 10 

matriz_principal = crear_matriz(dificultad,0)
lista_totalidad_navios = colocar_navios(matriz_principal)
matriz_rectangulos = dibujar_tablero(matriz_principal)
matriz_estado_celdas = crear_matriz(dificultad, False)
"""no hace falta xq se ejecuta en pantalla 2 sector de blit y draw"""
# crear_botones_tablero(matriz_rectangulos, matriz_estado_celdas)

# for i in range(len(lista_totalidad_navios)):
#     for j in range(len(lista_totalidad_navios[i])):
#         print(lista_totalidad_navios[i][j]["valor"])

# print(lista_totalidad_navios[i][j]["fila"])
# print(lista_totalidad_navios[i][j]["columna"])
# print(lista_totalidad_navios[i][j]["valor"])
# print(lista_totalidad_navios[i][j]["tocado"])




"############################################################################################################################"
#########################################################################################################################
"""############################################################################################################################"""
#########################################################################################################################
"""#########################################################################################################################"""




#BANDERAS_PANTALLAS:
bandera_sonido = True
bandera_ventana = 1
bandera_corriendo = True

#WHILE PRINCIPAL
puntos = 0
lista_puntos = [12,89,85,45,12]
while bandera_corriendo == True:

    # FOR PRINCIPAL
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_corriendo = False

        ############### BOTONES ##################
        ###########################################

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()

            if bandera_ventana == 1:

                if rectangulo_salir.collidepoint(pos_mouse): #Salir
                    bandera_corriendo = False

                if rectangulo_sonido.collidepoint(pos_mouse): #Sonido
                    if bandera_sonido == False:
                        bandera_sonido = True
                    else:
                        bandera_sonido = False
            
                if rectangulo_jugar.collidepoint(pos_mouse): #Jugar
                    bandera_ventana = 2
                
                if rectangulo_nivel.collidepoint(pos_mouse): #nivel
                    bandera_ventana = 3
                
                if rectangulo_puntaje.collidepoint(pos_mouse): #puntajes
                    bandera_ventana = 4

            if bandera_ventana == 2:
                matriz_rectangulos = dibujar_tablero(matriz_principal)
                crear_botones_tablero(matriz_rectangulos, matriz_estado_celdas)

                for i in range(len(matriz_principal)):
                    for j in range(len(matriz_principal[0])):
                        rectangulo = matriz_rectangulos[i][j]

                        if rectangulo.collidepoint(pos_mouse) and matriz_estado_celdas[i][j] == False:
                            
                            if matriz_principal[i][j] == 0:
                                if bandera_sonido == True:
                                    efecto_agua.play()
                            if matriz_principal[i][j] != 0:
                                if bandera_sonido == True:
                                    efecto_cañon.play()
                                puntos+=5
                                matriz_estado_celdas[i][j] = True
                                valor = gestionar_barcos_puntos(matriz_principal, matriz_estado_celdas,lista_totalidad_navios)
                                if valor > 1:
                                    puntos += (valor * 10)
                            if matriz_principal[i][j] == 0:
                                puntos -= 1
                                matriz_estado_celdas[i][j] = True

                            if verificar_barcos_vivos(lista_totalidad_navios) == False:
                                lista_puntos.append(puntos)
                                if bandera_sonido == True:
                                    efecto_victoria.play()
                                matriz_estado_celdas = crear_matriz(dificultad, True)

                            
            
                if rectangulo_reiniciar.collidepoint(pos_mouse):
                    matriz_principal = crear_matriz(dificultad,0)
                    lista_totalidad_navios = colocar_navios(matriz_principal)
                    matriz_estado_celdas = crear_matriz(dificultad, False)
                    puntos = 0


                if rectangulo_volver.collidepoint(pos_mouse): #Volver
                    bandera_ventana = 1
            


            if bandera_ventana == 3:
                if rectangulo_facil.collidepoint(pos_mouse):
                    dificultad = 10
                if rectangulo_medio.collidepoint(pos_mouse):
                    dificultad = 20
                if rectangulo_dificil.collidepoint(pos_mouse):
                    dificultad = 40
                """se regeneran los valores UNA sola vez porque se hizo click y volvemos al bucle que lo ejecuta"""
                puntos = 0
                matriz_principal = crear_matriz(dificultad,0)
                lista_totalidad_navios = colocar_navios(matriz_principal)
                matriz_estado_celdas = crear_matriz(dificultad, False)
                

                if rectangulo_volver.collidepoint(pos_mouse): #Volver
                    bandera_ventana = 1

            if bandera_ventana == 4:
                if rectangulo_volver.collidepoint(pos_mouse): #Volver
                    bandera_ventana = 1

            
            ############################################
            ############### BLIT Y DRAW ################
            ############################################ 
            
        """######## MENU PRINCIPAL (BANDERA 1)########"""

        if bandera_ventana == 1:

            #Imagen inicio
            ventana_principal.blit(imagen_inicio,(0,0))

            # Rectangulos/Botones
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_nivel,width=5, border_radius=5)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_jugar,width=5, border_radius=5)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_puntaje,width=5, border_radius=5)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_sonido,width=5, border_radius=5)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_salir,width=5, border_radius=5)
    
            #Textos
            ventana_principal.blit(texto_nivel,coordenadas_texto_nivel)
            ventana_principal.blit(texto_jugar,coordenadas_texto_jugar)
            ventana_principal.blit(texto_puntaje,coordenadas_texto_puntaje)
            ventana_principal.blit(texto_sonido,coordenadas_texto_sonido)
            ventana_principal.blit(texto_salir,coordenadas_texto_salir)

            """######## JUEGO (BANDERA 2)########"""
    
        if bandera_ventana == 2:
            #Imagen fondo (mar)
            ventana_principal.blit(imagen_fondo_tablero,(0,0))

            #unicas dos que tienen que estar iterando continuamente
            matriz_rectangulos = dibujar_tablero(matriz_principal)
            crear_botones_tablero(matriz_rectangulos, matriz_estado_celdas)

            # Volver
            texto_volver = fuente_volver.render("Volver", True, NEGRO,None)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_volver,width=5, border_radius=5)
            ventana_principal.blit(texto_volver, coordenadas_texto_volver)
            # Reiniciar
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_reiniciar,width=5, border_radius=5)
            ventana_principal.blit(texto_reiniciar,coordenadas_texto_reiniciar)

            #Puntaje
            texto_puntos = fuente_puntos.render(str(f"Puntos: {puntos:04d}"), True, NEGRO, GRIS)
            dimension_texto_puntos = texto_puntos.get_size()
            coordenadas_texto_puntos = ((ANCHO_VENTANA - dimension_texto_puntos[0] -20),coordenadas_texto_volver[1])
            ventana_principal.blit(texto_puntos, coordenadas_texto_puntos)

            """######## DIFICULTAD (BANDERA 3)########"""

        if bandera_ventana == 3:
            #Imagen timon
            ventana_principal.blit(imagen_fondo_niveles,(0,0))

            # Rectangulos/Botones
            pygame.draw.rect(ventana_principal,CHOCOLATE,rectangulo_facil,width=0, border_radius=5)
            pygame.draw.rect(ventana_principal,CHOCOLATE,rectangulo_medio,width=0, border_radius=5)
            pygame.draw.rect(ventana_principal,CHOCOLATE,rectangulo_dificil,width=0, border_radius=5)
    
            #Textos
            ventana_principal.blit(texto_facil,coordenadas_texto_facil)
            ventana_principal.blit(texto_medio,coordenadas_texto_medio)
            ventana_principal.blit(texto_dificil,coordenadas_texto_dificil)


            # Volver
            texto_volver = fuente_volver.render("Volver", True, CREMA,None)
            pygame.draw.rect(ventana_principal,CHOCOLATE,rectangulo_volver,width=0, border_radius=5)
            ventana_principal.blit(texto_volver, coordenadas_texto_volver)


            """######## PUNTAJES (BANDERA 4)########"""

        if bandera_ventana == 4:
            #Imagen saludo militar
            ventana_principal.blit(imagen_fondo_puntajes,(0,0))

            mostrar_top_5(lista_puntos)

            # Volver
            texto_volver = fuente_volver.render("Volver", True, BLANCO_MARINERO,None)
            pygame.draw.rect(ventana_principal,AZUL_MARINERO,rectangulo_volver,width=0, border_radius=5)
            ventana_principal.blit(texto_volver, coordenadas_texto_volver)


                



    # pygame.display.update()
    pygame.display.flip() 

pygame.quit()