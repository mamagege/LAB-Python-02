#Lab02 Python Funcional IAPP-2026-01
#Ejercicio 4 - Filter y Reduce - Juan Diego Gaitan

from functools import reduce


#Filter
#Realizar los siguientes ejercicios usando filter.

#a. Dada una lista de palabras, filtrar solo aquellas con mas de 4 letras.

palabras_mas_de_4 = list(filter(lambda p: len(p) > 4, ["Hola","Pepes","Oso","Juliana","Arroz","Xocas"]))
print(palabras_mas_de_4) #Output: ['Pepes', 'Juliana', 'Arroz', 'Xocas']

#b. Dada una lista filtrar los elementos que son nulos (None).

nulos = list(filter(lambda n: n is None, [None,"hola",None,"alooo"]))
print(nulos) #Output: [None, None]

#c. Dada una lista de palabras, filtrar aquellas que empiezan por una vocal.

empieza_vocal = list(filter(lambda p: p.lower()[0] in "aeiou", ["Arroz","Hola","Isabella","Jose","Uranio"]))
print(empieza_vocal) #Output: ['Arroz', 'Isabella', 'Uranio']

#d. Dada una lista de palabras, filtrar aquellas que son palindromos.

palindromos = list(filter(lambda p: p.lower() == p.lower()[::-1], ["Ana","Camilo","Oso","Aza","Soso"]))
print(palindromos) #Output: ['Ana', 'Oso', 'Aza']

#e. Dada una lista de numeros, filtrar los que terminan en 5.

termina_en_5 = list(filter(lambda n: n % 5 == 0 and n % 2 != 0, range(30)))
print(termina_en_5)

#f. Dada una lista de diccionarios, filtrar los productos con precio mayor a 100.

productos = [
    {"nombre": "Teclado", "precio": 80},
    {"nombre": "Mouse", "precio": 40},
    {"nombre": "Monitor", "precio": 300},
    {"nombre": "Webcam", "precio": 150}
]

precio_mayor_100 = list(filter(lambda p: p.get("precio") > 100, productos))
print(precio_mayor_100) #Output: [{'nombre': 'Monitor', 'precio': 300}, {'nombre': 'Webcam', 'precio': 150}]


#Reduce

#Realizar los siguientes ejercicios usando reduce.
#a. Dada una lista de numeros, calcula la multiplicación de estos.


multiplicacion_lista = reduce(lambda x,y: x*y,range(1,21))
print(multiplicacion_lista) #Output: 2432902008176640000

#b. Dada una lista de palabras, concetenalas en una sola.

concatenacion_palabras = reduce(lambda a,b: a +b, ["Hola"," ", "soy"," ","German","!"])
print(concatenacion_palabras) #Output: "Hola soy German!"

#c. Dada una lista, hallar el mayor de todos, define una función auxiliar que dado dos numeros retorne el mayor

mayor = lambda x,y: max(x,y)

mayor_de_todos = reduce(mayor,range(1,21))
print(mayor_de_todos) #Output: 20



