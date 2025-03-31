
# Day 18

import re
from collections import Counter

# Ejercicio Nivel 1 - 1: Palabra más frecuente en el párrafo
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Limpiar y obtener las palabras
words = re.findall(r'\b\w+\b', paragraph.lower())  # Convertir todo a minúsculas para evitar distinción de mayúsculas/minúsculas
word_count = Counter(words)

# Imprimir la palabra más frecuente
print("Ejercicio 1: Palabra más frecuente")
print(word_count.most_common(), "\n")

# Ejercicio Nivel 1 - 2: Distancia entre los puntos más alejados
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = sorted(map(int, points))  # Convertir los puntos a enteros y ordenar
distance = sorted_points[-1] - sorted_points[0]  # La distancia entre el punto más lejano y el más cercano

print("Ejercicio 2: Distancia entre los puntos más alejados")
print(f'Distancia entre los puntos más alejados: {distance}\n')

