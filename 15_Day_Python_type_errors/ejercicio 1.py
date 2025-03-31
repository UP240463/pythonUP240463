
# Day 15

# 1. SyntaxError (Error de sintaxis)
# El siguiente código da un SyntaxError porque falta poner los paréntesis en la función print
# Solución: colocar los paréntesis correctamente.

# print 'Hola mundo'  # Esto da un SyntaxError en Python 3
print('Hola mundo')  # Esto es correcto

# 2. NameError (Error de nombre)
# El siguiente código da un NameError porque intentamos acceder a una variable no definida.
# Solución: definir la variable antes de usarla.

# print(edad)  # Esto da un NameError porque 'edad' no está definida
edad = 25  # Definimos la variable
print(edad)  # Imprime 25

# 3. IndexError (Error de índice)
# El siguiente código da un IndexError porque intentamos acceder a un índice fuera del rango de la lista.
# Solución: asegurarnos de que el índice esté dentro del rango válido.

numeros = [1, 2, 3, 4, 5]
# print(numeros[5])  # Esto da un IndexError, ya que el índice 5 está fuera del rango (0-4)
print(numeros[4])  # Esto es correcto, imprime 5

# 4. ModuleNotFoundError (Error de módulo no encontrado)
# El siguiente código da un ModuleNotFoundError porque intentamos importar un módulo inexistente.
# Solución: importar el módulo correcto.

# import matematicas  # Esto da un ModuleNotFoundError
import math  # Esto es correcto, se importa el módulo math
print(math.sqrt(16))  # Imprime 4.0 (raíz cuadrada de 16)

# 5. AttributeError (Error de atributo)
# El siguiente código da un AttributeError porque estamos intentando acceder a un atributo que no existe.
# Solución: corregir el nombre del atributo.

# print(math.PI)  # Esto da un AttributeError porque 'PI' no existe, debería ser 'pi'
print(math.pi)  # Esto es correcto, imprime el valor de pi (3.141592653589793)

# 6. KeyError (Error de clave)
# El siguiente código da un KeyError porque intentamos acceder a una clave inexistente en un diccionario.
# Solución: usar una clave válida que exista en el diccionario.

usuarios = {'nombre': 'Juan', 'edad': 30, 'pais': 'México'}
# print(usuarios['ciudad'])  # Esto da un KeyError, ya que 'ciudad' no es una clave válida
print(usuarios['pais'])  # Esto es correcto, imprime 'México'

# 7. TypeError (Error de tipo)
# El siguiente código da un TypeError porque estamos intentando sumar un número con una cadena.
# Solución: convertir la cadena a un número entero o viceversa.

# print(4 + '3')  # Esto da un TypeError porque no se puede sumar un entero con una cadena
print(4 + int('3'))  # Convertimos la cadena a entero, imprime 7

# 8. ImportError (Error de importación)
# El siguiente código da un ImportError porque intentamos importar una función inexistente de un módulo.
# Solución: importar la función correcta.

# from math import power  # Esto da un ImportError porque 'power' no existe en el módulo math
from math import pow  # Esto es correcto, 'pow' es la función adecuada
print(pow(2, 3))  # Imprime 8.0 (2 elevado a la 3)

# 9. ValueError (Error de valor)
# El siguiente código da un ValueError porque estamos intentando convertir una cadena con caracteres no numéricos en un número.
# Solución: asegurarse de que la cadena tenga un formato numérico adecuado.

# print(int('12a'))  # Esto da un ValueError porque '12a' no puede ser convertido a entero
print(int('12'))  # Esto es correcto, convierte la cadena '12' a 12

# 10. ZeroDivisionError (Error de división por cero)
# El siguiente código da un ZeroDivisionError porque intentamos dividir por cero.
# Solución: evitar la división por cero.

# print(1/0)  # Esto da un ZeroDivisionError
print(1/2)  # Esto es correcto, imprime 0.5
