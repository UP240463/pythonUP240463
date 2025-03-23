# Dia 10

# Nivel 1

# 1. Iterar de 0 a 10 usando un bucle for y un bucle while:
# Usando bucle for
print("Iteración de 0 a 10 usando for:")
for i in range(11):
    print(i)

# Usando bucle while
print("\nIteración de 10 a 0 usando while:")
i = 0
while i <= 10:
    print(i)
    i = i + 1

# 2. Iterar de 10 a 0 usando un bucle for y un bucle while:
# Usando bucle for
print("\nIteración de 10 a 0 usando for:")
for i in range(10, -1, -1):
    print(i)

# Usando bucle while
print("\nIteración de 10 a 0 usando while:")
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Imprimir un triángulo de '#':
print("\nImprimir triángulo con bucle:")
for i in range(1, 8):
    print('#' * i)

# 4. Usar bucles anidados para crear una cuadrícula de '#':
print("\nCuadrícula de # con bucles anidados:")
for i in range(8):  # 8 filas
    for j in range(8):  # 8 columnas
        print('#', end=' ')
    print()  # Pasar a la siguiente línea después de cada fila

# 5. Imprimir tabla de multiplicar del 0 al 10:
print("\nTabla de multiplicar del 0 al 10:")
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# 6. Iterar a través de la lista y imprimir cada ítem:
fruits = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
print("\nImprimir elementos de la lista:")
for item in fruits:
    print(item)

# 7. Imprimir solo números pares del 0 al 100:
print("\nNúmeros pares del 0 al 100:")
for i in range(0, 101, 2):
    print(i)

# 8. Imprimir solo números impares del 0 al 100:
print("\nNúmeros impares del 0 al 100:")
for i in range(1, 101, 2):
    print(i)
