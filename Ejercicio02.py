#Lab02 Python Funcional IAPP-2026-01

#Ejercicio 2 - listas de compresión - Juan Diego Gaitan

#1. Realizar los siguientes ejercicios usando listas de compresión.
#a. Generar una lista con tuplas (n, n^2) para una lista de numeros
tuplas = [(n,n*n) for n in range(1,10)]

print(tuplas) #Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]

#b. Generar una lista con cubos de los números mayores a 10.

cubos_mayores_10 = [n**3 for n in range(1,20) if n > 10]
print(cubos_mayores_10) #Output: [1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]


#c. Generar una lista con solo los numeros pares.

pares = [n for n in range(1,21) if n % 2 == 0]
print(pares) #Ouuput: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#d. Dada la lista numeros, producir:

#    ["valor: 10", "valor: 15", ...]

formato_valor = [f"valor: {n}" for n in range(10,26) if n % 5 == 0]
print(formato_valor) #Output: ['valor: 10', 'valor: 15', 'valor: 20', 'valor: 25']

#e. Generar una lista con la conversion correspondiente a grados Fahrenheit.

conversion_a_farenheit = [(n*1.8)+32 for n in range(0,21)]
print(conversion_a_farenheit) #Output: [32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0, 51.8, 53.6, 55.400000000000006, 57.2, 59.0, 60.8, 62.6, 64.4, 66.2, 68.0]

#f. Generar una lista filtrando las palabras de mas de 5 letras.

palabras_mas_5_letras = [palabra for palabra in ["hola","como","estamos","profesor","esperos","este","superrr"] if len(palabra) > 5 ]
print(palabras_mas_5_letras) #Output: ['estamos', 'profesor', 'esperos', 'superrr']

#g. Generar una lista con solo las iniciales de las palabras.

iniciales_palabras = [p[0] for p in ["Jose","Urunio","Ana","Niño","Diaz","Iglesia"]]
print(iniciales_palabras) #Output: ['J', 'U', 'A', 'N', 'D', 'I']

#h. Generar una lista indicando "par" o "impar" dada una lista de numeros.

par_impar = [f"{n} es par" if n % 2 == 0 else f"{n} es impar" for n in range(0,21)]
print(par_impar) #Output: ['0 es par', '1 es impar', '2 es par', '3 es impar', '4 es par', '5 es impar', '6 es par', '7 es impar', '8 es par', '9 es impar', '10 es par', '11 es impar', '12 es par', '13 es impar', '14 es par', '15 es impar', '16 es par', '17 es impar', '18 es par', '19 es impar', '20 es par']
#i. Dada una lista de listas (matriz), aplanala.

#    [[1,2,3], [4,5,6], [7,8,9]] = [1,2,3,4,5,6,7,8,9]

matriz = [[3,4,5],[6,7,8],[0,0,9],[1,2,3]]
aplanar_matriz = [n for x in matriz for n in x] #Output: [3, 4, 5, 6, 7, 8, 0, 0, 9, 1, 2, 3]
print(aplanar_matriz)
