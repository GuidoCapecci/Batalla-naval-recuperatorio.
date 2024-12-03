import random
import pygame
from configuraciones import *

#CREAR MATRIZ:
#################################################################################
#################################################################################

def crear_matriz(dificultad: int, valor: int | str | bool) -> list:
    """
    Recibe un entero (dificultad) y un valor, y genera una matriz cuadrada de tamaño `dificultad x dificultad` 
    con el valor proporcionado en cada celda.
    Parámetros:
    dificultad (int): El tamaño de la matriz (número de filas y columnas).
    valor (int | str | bool): El valor que se asignará a cada celda de la matriz.
    Retorna:
    list: Una matriz (lista de listas) con el valor asignado.
    """
    filas = dificultad
    columnas = dificultad

    matriz=[]
    
    for i in range(filas):
        fila=[]
        matriz+=[fila]
        for j in range(columnas):
            fila+=[valor]
    return matriz

#MOSTRAR MATRIZ
#################################################################################
#################################################################################

def mostrar_matriz(matriz: list) -> None:
    """
    Recibe una matriz y la imprime en consola, mostrando sus valores fila por fila.
    Parámetros:
    matriz (list): La matriz que se desea imprimir.
    Retorna:
    None
    """
    if type(matriz) != list:
        print("Debe ingresar una matriz")
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                print(matriz[i][j], end=" ")
            print(" ")

#COLOCAR NAVIOS:

def colocar_navios(matriz: list):
    """
    Coloca los barcos en una matriz de manera aleatoria según el tamaño de la matriz.
    Devuelve una lista de los barcos colocados, representados por bloques en la matriz.
    Parámetros:
    matriz (list): La matriz donde se colocarán los barcos.
    Retorna:
    list: Una lista de barcos representados como bloques dentro de la matriz.
    """

    dimension_matriz= len(matriz)

    lista_barcos_colocados=[]

    match dimension_matriz:
        case 10:
            cantidad_submarino = 4
            cantidad_destructores = 3
            cantidad_cruceros = 2
            cantidad_acorazados = 1
        case 20:
            cantidad_submarino =8
            cantidad_destructores =6
            cantidad_cruceros =4
            cantidad_acorazados =2
        case 40:
            cantidad_submarino =12
            cantidad_destructores =9
            cantidad_cruceros =6
            cantidad_acorazados =3

    lista_valor=[1,2,3,4]
    lista_largo=[1,2,3,4]
    lista_tipos = ["submarino","destructor","crucero","acorazado"]
    lista_cantidades=[cantidad_submarino,cantidad_destructores,cantidad_cruceros,cantidad_acorazados]

    for i in range(len(lista_tipos)):

        contador_colocados=0

        while  contador_colocados < lista_cantidades[i]:

            fila_inicial = random.randint(0,len(matriz) - (lista_largo[i])) #yo tenia (largo+1)
            columna_inicial = random.randint(0, len(matriz[0]) - (lista_largo[i])) #yo tenia (largo+1)
            orientacion = random.choice(["H", "V"])
            lista_un_barco=[]
            if validar_casilleros(matriz, fila_inicial, columna_inicial, lista_largo[i], orientacion) == True:
                contador_colocados += 1
                for j in range(lista_largo[i]):
                    if orientacion == "H":
                        matriz[fila_inicial][columna_inicial + j] = lista_valor[i]  # Coloca el barco horizontalmente
                        un_bloque = {"fila": fila_inicial, "columna": columna_inicial + j, "valor": lista_valor[i], "tocado": False, "hundido" : False }  # Guarda un bloque
                    else:
                        matriz[fila_inicial + j][columna_inicial] = lista_valor[i]  # Coloca el barco verticalmente
                        un_bloque = {"fila": fila_inicial + j, "columna": columna_inicial, "valor": lista_valor[i], "tocado": False, "hundido" : False }  # Guarda un bloque
                    
                    lista_un_barco.append(un_bloque)  # Agrega el bloque al barco
            
                lista_barcos_colocados.append(lista_un_barco)
    return lista_barcos_colocados

#VALIDAR CASILLEROS:
#########################################################################
#########################################################################
def validar_casilleros(matriz:list,fila:int, columna:int, largo:int, orientacion:str):
    """
    recibe una matriz, una fila, una columna, el largo del objeto que se quiere colocar
    y la orientacion del objeto ("H"/"V")
    verifica que todos los espacios necesarios sean del valor 0 y devuelve true.
    si algun casillero es distinto a 0 devuelve false.
    """
    bandera_vacio = True
    contador = 0
    if orientacion == "H" and (columna + largo) <= len(matriz[0]):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            columna += 1
            contador += 1

    if orientacion == "V" and (fila + largo) <= len(matriz):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            fila += 1
            contador += 1
    
    return bandera_vacio

#CENTRAR OBJETOS:
###################################################################
###################################################################
def centrar_objetos(ancho_rectangulo_fondo:int,alto_rectangulo_fondo:int,ancho_rectangulo_colocar:int,alto_rectangulo_colocar:int):
    """
    Calcula las coordenadas para centrar un rectángulo dentro de otro.
    Parámetros:
    ancho_rectangulo_fondo (int): Ancho del rectángulo de fondo.
    alto_rectangulo_fondo (int): Alto del rectángulo de fondo.
    ancho_rectangulo_colocar (int): Ancho del rectángulo a colocar.
    alto_rectangulo_colocar (int): Alto del rectángulo a colocar.
    Retorna:
    list: Coordenadas [eje_x_centrado, eje_y_centrado] para colocar el rectángulo centrado.
    """

    mitad_ancho_fondo = ancho_rectangulo_fondo // 2
    mitad_ancho_colocar = ancho_rectangulo_colocar // 2

    eje_x_centrado = mitad_ancho_fondo - mitad_ancho_colocar

    mitad_alto_fondo = alto_rectangulo_fondo // 2
    mitad_alto_colocar = alto_rectangulo_colocar // 2

    eje_y_centrado = mitad_alto_fondo - mitad_alto_colocar

    # eje_x_centrado = (ancho_rectangulo_fondo - ancho_rectangulo_colocar) // 2
    # eje_y_centrado = (alto_rectangulo_fondo - alto_rectangulo_colocar) // 2

    coordenadas=[eje_x_centrado,eje_y_centrado]

    return coordenadas

#CENTRAR OBJETOS2:
def centrar_objetos_2(rectangulo_fondo:tuple|list, rectangulo_colocar:tuple|list, pos_rectangulo:tuple|list):
    """
    Centra un objeto dentro de un fondo con base en la posición proporcionada.
    Parámetros:
    rectangulo_fondo (tuple): Tamaño del fondo (ancho, alto).
    rectangulo_colocar (tuple): Tamaño del objeto a centrar (ancho, alto).
    pos_rectangulo (tuple): Posición inicial del objeto dentro del fondo (x, y).
    Retorna
    list: Coordenadas (x, y) centradas para colocar el objeto dentro del fondo.
    """
    rectangulo_x = pos_rectangulo[0]
    rectangulo_y = pos_rectangulo[1]

    #PASO 1
    ancho_fondo = rectangulo_fondo[0]
    alto_fondo = rectangulo_fondo[1]
    #PASO 2
    ancho_colocar = rectangulo_colocar[0]
    alto_colocar = rectangulo_colocar[1]
    #PASO 3
    mitad_ancho_fondo = ancho_fondo // 2
    mitad_alto_fondo = alto_fondo // 2
    #PASO 4
    mitad_ancho_colocar = ancho_colocar // 2
    mitad_alto_colocar = alto_colocar // 2
    #PASO 5
    eje_x_centrado = (mitad_ancho_fondo - mitad_ancho_colocar) + rectangulo_x
    eje_y_centrado = (mitad_alto_fondo - mitad_alto_colocar) + rectangulo_y

    coordenada_centrada = [eje_x_centrado,eje_y_centrado]
    return coordenada_centrada


#CENTRAR EJE_X:
###################################################################
###################################################################

def centrar_eje_x(ancho_fondo:int, ancho_colocar:int):
    """
    Calcula la coordenada x para centrar un objeto dentro de un fondo.
    Parámetros:
    ancho_fondo (int): Ancho del fondo.
    ancho_colocar (int): Ancho del objeto a centrar.
    Retorna:
    int: Coordenada x para posicionar el objeto de manera centrada en el fondo.
    """

    centro_fondo = ancho_fondo //2
    centro_colocar = ancho_colocar//2

    eje_x_centrado = centro_fondo - centro_colocar

    return eje_x_centrado

###################################################################
###################################################################

def gestionar_barcos_puntos (matriz_principal:list, matriz_estado:list, lista_barcos:list)->int:
    """
    Gestiona el estado de los barcos y asigna puntos según si se hunden o se tocan.
    Parámetros:
    matriz_principal (list)
    matriz_estado (list): Matriz que guarda el estado de cada celda.
    lista_barcos (list): Lista de diccionarios que representa los barcos y su estado.
    Retorna:
    int: El valor del largo del barco hundido o 0 si no se ha hundido ningún barco.
    """
    retorno = 0
    for i in range(len(matriz_principal)):
        for j in range(len(matriz_principal[0])):

            verificar_barcos(lista_barcos, i,j,matriz_estado[i][j])
            largo_navio_hundido = verificar_estado_barcos(lista_barcos)

            if largo_navio_hundido > 1:
                retorno = largo_navio_hundido
                break
    return retorno


def verificar_barcos(lista_barcos, fila, columna, estado_matriz)->None:
    """
    Verifica si un barco ha sido tocado y actualiza su estado.
    Parámetros:
    lista_barcos (list): Lista de barcos representados como diccionarios.
    fila (int): Fila de la matriz donde se hizo el disparo.
    columna (int): Columna de la matriz donde se hizo el disparo.
    estado_matriz (bool): El estado de la celda (si está tocada o no).

    No retorna valor, actualiza el estado de los barcos en la lista.
    """
    for i in range(len(lista_barcos)):
        for j in range(len(lista_barcos[i])):

            fila_bloque = lista_barcos[i][j]["fila"]
            columna_bloque = lista_barcos[i][j]["columna"]
            valor_bloque = lista_barcos[i][j]["valor"]
            tocado_bloque = lista_barcos[i][j]["tocado"]

            if (fila == fila_bloque) and (columna == columna_bloque) and (estado_matriz == True):

                lista_barcos[i][j]["tocado"] = True


def verificar_estado_barcos (lista_barcos:list)->int:
    """
    Verifica si todos los bloques de un barco han sido tocados, lo marca como hundido y retorna su valor.
    Parámetros:
    lista_barcos (list): Lista de barcos representados como diccionarios.
    Retorna:
    int: El valor del barco si se ha hundido, 0 si no se ha hundido ningún barco.
    """
    valor = 0
    bandera_tocado = False
    for i in range(len(lista_barcos)):
        for j in range(len(lista_barcos[i])):

            if lista_barcos[i][j]["tocado"] == True and lista_barcos[i][j]["hundido"] == False:
                bandera_tocado=True
            else:
                bandera_tocado=False
                break

        if bandera_tocado == True:
            lista_barcos[i][j]["hundido"] = True
            valor = lista_barcos[i][j]["valor"]
            break

    return valor


def verificar_barcos_vivos (lista_barcos)->bool:
    """
    Verifica si hay barcos aún no hundidos.
    Parámetros:
    lista_barcos (list): Lista de barcos representados como diccionarios.
    Retorna:
    bool: `True` si hay barcos vivos, `False` si todos los barcos están hundidos.
    """
    retorno = True
    cantidad_navios = len(lista_barcos)
    contador = 0
    for i in range(len(lista_barcos)):
        for j in range(len(lista_barcos[i])):

            if lista_barcos[i][j]["hundido"] == True:
                contador += 1
    if contador == cantidad_navios:
        retorno = False
    return retorno



def ordenar_lista(lista: list, orden: str) -> list:
    """
    Ordena una lista en orden ascendente o descendente según el parámetro 'orden'.
    Parámetros:
    lista (list): Lista de elementos a ordenar.
    orden (str): Puede ser "ASC" para orden ascendente o "DESC" para descendente.
    Retorna:
    list: La lista ordenada o la misma lista si tiene un solo elemento.
    """

    if len(lista) > 1:
      
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if (orden == "ASC" and lista[i] > lista[j]) or (orden == "DESC" and lista[i] < lista[j]):
                    temp = lista[i]
                    lista[i] = lista[j]
                    lista[j] = temp   
                
    return lista







    
    

