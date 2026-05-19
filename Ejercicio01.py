#Lab02 Python Funcional IAPP-2026-01

#Ejercicio 1 - Funciones lambdas. Juan Diego Gaitán

#A) Definir las siguientes funciones usando lambdas.

#a. Crear una lambda que reciba un número y devuelva True si es múltiplo de 3, False en caso contrario.

multiplo_3 = lambda n: True if n % 3 == 0 else False

print(multiplo_3(4)) #Output: False

#b. Crear una lambda que reciba un número y devuelva su cubo.

cubo = lambda n: n**3

print(cubo(4)) #Output: 64

#c. Crear una lambda que reciba dos números y devuelva su producto.

producto = lambda x,y: x * y

print(producto(5,2)) #Output: 10

#d. Crear una lambda que reciba dos números y devuelva el mayor.

mayor = lambda x,y: max(x,y)

print(mayor(-2,900)) #Output: 900

#e. Crear una lambda que reciba una palabra y devuelva True si empieza con la letra “A" (o “a”).

palabra_inicia_con_a = lambda p: True if p.lower().startswith("a") else False

print(palabra_inicia_con_a("Arróz")) #Output: True

#f. Crear una lambda que reciba una temperatura en Celsius y la convierta a Fahrenheit.

conversion_a_farenheit = lambda t: (t*1.8) + 32

print(conversion_a_farenheit(20)) #Output: 68


#B) Realizar el siguiente ejercicio usando lambdas

#Crear una lista que contenga tres lambdas:

operaciones = [lambda n: n*2, lambda n: n + 10, lambda n: n*n]
numero_usuarios = int(input("Ingrese un número: "))
for operacion in operaciones: 
    print(operacion(numero_usuarios))


#Una que duplique un número
#Una que le sume 10
#Una que calcule su cuadrado
#Luego, pedir un número al usuario y aplicar cada lambda a ese número, mostrando los resultados.

#Ingrese un número: 5
#10
#15
#25