#Lab02 Python Funcional IAPP-2026-01
#Ejercicio 5 - Sorted

from functools import reduce



#Realizar los siguientes ejercicios usando sorted.
#a. Ordenas una lista de palabras alfabeticamente.

ordenado_alfa = sorted(["Hola","Aba","Abeja","Carro","Bubalu","Avestruz"])
print(ordenado_alfa) #Output: ['Aba', 'Abeja', 'Avestruz', 'Bubalu', 'Carro', 'Hola']

#b. Ordenar una lista de tuplas por el primer elemento.

primer_elemento = sorted([(1,"Abe"),(10,"Arroz"),(0,"Camion"), (13,"Hola"),(5,"Fiesta")], key=lambda t: t[0])
print(primer_elemento) #Output: [(0, 'Camion'), (1, 'Abe'), (5, 'Fiesta'), (10, 'Arroz'), (13, 'Hola')]

#c. Dada una lista de tuplas, ordenar por precio (mayor a menor), y luego por nombre

productos = [
      ("Camisa", 30),
      ("Pantalón", 55),
      ("Medias", 10),
      ("Chaqueta", 80)
  ]

mayor_precio_nombre = sorted(productos, key=lambda d: (-d[1], d[0]))
print(mayor_precio_nombre) #Output: [('Chaqueta', 80), ('Pantalón', 55), ('Camisa', 30), ('Medias', 10)]

#d. Dada una lista de palabras, ordenarlas según su longitud.

orden_longitud = sorted(["Hola","Arrroooz","H"," ","Papa","Papas","Esternocleido","Oso","Aza"], key= lambda p: (len(p), p))
print(orden_longitud) #Output: [' ', 'H', 'Aza', 'Oso', 'Hola', 'Papa', 'Papas', 'Arrroooz', 'Esternocleido']

#e. Dada una lista de numeros, ordenarlos de tal forma que aparezcan primero los pares y luego los impares.

pares_impares = sorted(range(30), key=lambda n: n % 2)
print(pares_impares) #Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

#f. Convertir una palabra a un diccinario que cuente la aparicion de cada letra, ordenar dicho diccionario según la frecuencia de aparicion.

def contador_palabras(palabra):
    palabra = palabra.lower()
    diccionario = dict()

    for letra in palabra:
        diccionario[letra] = diccionario.get(letra,0) + 1
    return diccionario

palabra = "Hola soy german garmendia el rey de roma y me encanta la pasta"
contador_ordenado = sorted(contador_palabras(palabra).items(),key=lambda p: p[1], reverse=True)
print(dict(contador_ordenado)) #Output: {' ': 12, 'a': 10, 'e': 7, 'r': 4, 'm': 4, 'n': 4, 'o': 3, 'l': 3, 'y': 3, 's': 2, 'g': 2, 'd': 2, 't': 2, 'h': 1, 'i': 1, 'c': 1, 'p': 1}

#g. Dada una lista de tuplas, ordenar la primera por el departamento del empleado y luego por la edad.

empleados = [
      ("Maria", "Ventas", 30),
      ("Luis", "Tecnología", 25),
      ("Ana", "Ventas", 25),
      ("Pedro", "Tecnología", 28)
    ]

departamentos_ordenados = sorted(empleados, key=lambda t: (t[1],t[2]))
print(departamentos_ordenados) #Output: [('Luis', 'Tecnología', 25), ('Pedro', 'Tecnología', 28), ('Ana', 'Ventas', 25), ('Maria', 'Ventas', 30)]

#Usando map, filter, reduce y/o sorted

#h. Filtrar números pares y luego elevarlos al cuadrado.

par = list(filter(lambda n: n % 2 == 0, range(30)))
par_cuadrado = list(map(lambda n: n**2, par))
print(par_cuadrado) #Output: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]

#i. Dada una lista de numeros, elevar cada número al cubo, filtrar los mayores que 100, convertirlos a cadenas.

cubo = list(map(lambda n: n**3, range(30)))
cubo_filtrado = list(filter(lambda n: n > 100, cubo))
cubo_filtrado_cadena = list(map(str, cubo_filtrado))
print(cubo_filtrado_cadena) #Output: ['125', '216', '343', '512', '729', '1000', '1331', '1728', '2197', '2744', '3375', '4096', '4913', '5832', '6859', '8000', '9261', '10648', '12167', '13824', '15625', '17576', '19683', '21952', '24389']


#j. Dada una lista de numeros, filtrar números mayores que 10, elevarlos al cuadrado, ordenarlos de mayor a menor.

mayores_10_cuadrados_ordenados = sorted(map(lambda n: n **2, filter(lambda n: n > 10, range(30))), reverse= True)
print(mayores_10_cuadrados_ordenados) #Output: [841, 784, 729, 676, 625, 576, 529, 484, 441, 400, 361, 324, 289, 256, 225, 196, 169, 144, 121]
