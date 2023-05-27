# def suma(num1, num2):
#     return num1+num2

# def resta(num1, num2):
#     return num1-num2

# def multiplica(num1, num2):
#     return num1*num2

# def divide(num1,num2):
#     try:
#      return num1/num2
#     except ZeroDivisionError:
#         print("No se puede dividir entre cero")
#         return "Operación Errónea"


# op1=(int(input("Introduce el primer número: ")))

# op2=(int(input("Introduce el segundo número: ")))

# operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

# if operacion=="suma":
#     print(suma(op1,op2))

# elif operacion=="resta":
#     print(resta(op1,op2))

# elif operacion=="multiplica":
#     print(multiplica(op1,op2))

# elif operacion=="divide":
#         print(divide(op1,op2))


# else:
#     print ("Operación no contemplada")

# print("Operación ejecutada. Continuación de ejecúción del programa ")

# try:
#     op1=(int(input("Introduce el primer número: ")))

#     op2=(int(input("Introduce el segundo número: ")))

#     operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
#     if operacion=="suma":
#         print(suma(op1,op2))

#     elif operacion=="resta":
#         print(resta(op1,op2))

#     elif operacion=="multiplica":
#         print(multiplica(op1,op2))

#     elif operacion=="divide":
#         print(divide(op1,op2))


#     else:
#         print ("Operación no contemplada")

# except ValueError:
#      print("No se aceptan caracteres que no sean números")


# print("Operación ejecutada. Continuación de ejecúción del programa ")

# def divide():

#     try:
#         op = float(input("Introduce un número: "))
#         op2 = float(input("Introduce un número: "))
#         print("La división es: ", str(op/op2))
#     except ZeroDivisionError:
#         print("Error! No se puede dividir por 0.")
#     except ValueError:
#         print("Error! El caracter ingresado no es valido.")
#     finally:
#         print("Calculo finalizado")

# divide()

#---generadores---
#Estructura básica

# def generador():
#     n = 1
#     yield n

#     n += 1
#     yield n

#     n += 1
#     yield n

# g = generador()
# print(next(g))
# print(next(g))
# print(next(g))

# def generaPares(limite):
#     num = 1
#     miListado = []
#     while num < limite:
#         miListado.append(num*2)
#         num += 1
#     return miListado
# print(generaPares(10))

# def generaPares(limite):
#     num = 1
#     while num < limite:
#         num = num * 2
        
#         yield num 
    #return miListado
#print(generaPares(10))
# r = generaPares(18)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

# def generaNumeros(limite):
#     num = 0
#     while num < limite:
#         yield num + 1
        
# g = generaNumeros(100)

# for i in g:
#     print(i)


#Otro ejemplo

# def devuelveCiudades(*ciudades):
#     for elementos in ciudades:
#         for caracter in elementos:
#             yield caracter
            

# ciudad = devuelveCiudades("medellin", "bogota", "cali", "cartagena")

# print(next(ciudad))
# print(next(ciudad))


# def numeros_0_9():
#     num = 0
#     limite = 9
#     while num <= limite: 
#         num = num + 1       
#         yield num

# def numeros_10_20():
#     num = 10
#     limite = 20
#     while num <= limite:        
#         yield num
#         num += 1

# num1 = numeros_0_9()
# print(next(num1))

# def result():
#     num1 = numeros_0_9()
#     num2 = numeros_10_20()
#     for i in num1:
#         print(i)
#     for i in num2:
#         print(i)

# r = result()


# print("------------------------------")
# import random

# def generador():
#         print(random.randint(1, 100))      
#         print(random.randint(1, 100))      
#         print(random.randint(1, 100))      
#         print(random.randint(1, 100))      
#         print(random.randint(1, 100))      
#         print(random.randint(1, 100))      
#         print(random.randint(1, 100))      
              

#f = generador()
#print(f)

#Si se importa la biblioteca entera, se debe escribir el nombre de la biblioteca y el de la 
#función separada por un punto, como muestra el siguiente ejemplo:

# import random

# print(random.randrange(10))

#Si se importa únicamente una función, se debe escribir simplemente el nombre de la función, 
#como muestra el siguiente ejemplo:

# from random import *#randrange

# print(randrange(10))

#Si se importan varias funciones, los nombres de las 
#funciones deben separarse como comas (,), como muestra 
#el siguiente ejemplo:
#choice devuelve un elemento aleatorio de una lista:

# from random import randrange, choice

# print(randrange(10))
# print(choice(["uno", "dos", "tres"]))

#Generar números enteros: la función randrange()  
#La función randrange(a, b, c) genera un número entero entre 
#los valores generados por range(a, b, c). Como ocurre con range(), la función randrange()
#admite uno, dos o tres argumentos.

# print(randrange(10,110,10))

#Generar números enteros: la función randint()
#La función randint(a, b) genera un número entero entre a y b, ambos incluidos. a debe ser 
#inferior o igual a b.

# print(random.randint(10,20))

#Generar números decimales: la función random() 
#La función random() genera un número decimal entre 0 y 1 (puede generar 0, pero no 1).

# print(random.random())

#Generar números decimales: la función uniform() 
#La función uniform(a, b) genera un número decimal entre a y b (puede generar a y, debido a la 
#forma de redondear de Python, puede que genere b o no).

# print(random.uniform(5,8))

#Seleccionar un elemento al azar: la función choice() 
#La función choice(secuencia) elige un valor al azar en un conjunto de 
#elementos. Cualquier tipo de datos enumerable (tupla, lista, cadena, range) 
#puede utilizarse como conjunto de elementos.

# print(random.choice(14, 15, 20, 30))

# print(random.choice("Piña","Manzana","Pera"))

# print(random.choice(range(10)))


# import random

# def comida_hoy():
#     print(random.choice(["Frijoles","Sudado","Lentejas","Sopa"]))

# comida_hoy()

#Si se importa la biblioteca entera, se debe escribir el nombre de la biblioteca y el de la 
#función separada por un punto, como muestra el siguiente ejemplo:

# import time

# print(time.localtime())

#Si se importa únicamente una función, se debe escribir simplemente el nombre de la función, 
#como muestra el siguiente ejemplo:

# from time import localtime

# print(localtime())

#•	Si se importan varias funciones, los nombres de las funciones deben separarse como comas (,), 
# como muestra el siguiente ejemplo:

#from time import localtime, asctime, time

# print(asctime(localtime()))

#•	Segundos desde el origen: la función time()
#La función time() devuelve el número de segundos transcurridos desde el origen de los tiempos del
#sistema, que suele ser el 1 de enero de 1970. El resultado es un número decimal, pero la precisión
#en los decimales depende del ordenador.


#print(time.time())

import time

inicio = time.time()

for i in range(5000):
    print(f"{i} - ", end="")
final = time.time()

print(f"He tardado {round(final - inicio, 1)} segundos.")