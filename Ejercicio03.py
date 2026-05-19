#Lab02 Python Funcional IAPP-2026-01
#Ejercicio 3 - Map - Juan Diego Gaitan

import math


#1. Realizar los siguientes ejercicios usando map: 

#a. Dada una lista de temperaturas en Celsius, convertirlas a Fahrenheit.

celsius_a_farenheit = list(map(lambda t: (t*1.8) + 32,range(13)))
print(celsius_a_farenheit) #Output: [32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0, 51.8, 53.6]

#b. Dadas dos listas con la misma cantidad de elementos, generar una nueva sumando cada elementos (primer elemento de lista 1 + primer elemento lista 2).

suma_listas = list(map(lambda l1,l2: l1 + l2, range(11), range(-5,6)))
print(suma_listas) #Output: [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]

#c. Dada una lista de radios de circulos, generar la lista de sus areas.

area_circulos = list(map(lambda r: math.pi * r**2, range(15)))
print(area_circulos) #Output: [0.0, 3.14, 12.56, 28.259999999999998, 50.24, 78.5, 113.03999999999999, 153.86, 200.96, 254.34, 314.0, 379.94, 452.15999999999997, 530.66, 615.44]

#d. Dada un diccionario, generar una lista de tuplas (nombre, valor+10%)

#  {"pan": 1000, "leche": 2500, "café": 5000}

productos = {
    "pan":1000,
    "leche":2500,
    "café":5000,
    "huevos":100
}

productos_con_iva = list(map(lambda p: (p[0],p[1]*1.1), productos.items()))
print(productos_con_iva) #Output: [('pan', 1100.0), ('leche', 2750.0), ('café', 5500.0), ('huevos', 110.0)]


#e. Dada una matriz, multiplicar todos los elementos por 10.

matriz = [[0,8,4],[1,2,3],[6,7,7],[5,-5,1]]

multiplicar_por_10 = list(map(lambda x: x*10,[n for f in matriz for n in f]))
print(multiplicar_por_10) #Output: [0, 80, 40, 10, 20, 30, 60, 70, 70, 50, -50, 10]