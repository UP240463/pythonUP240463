# Dia 11

# Nivel 1

# 1. Declarar una función add_two_numbers que toma dos parámetros y devuelve la suma
def add_two_numbers(a, b):
    return a + b

# 2. Función para calcular el área de un círculo
import math
def area_of_circle(r):
    return math.pi * r * r

# 3. Función add_all_nums que toma un número arbitrario de argumentos y suma todos
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números"

# 4. Función para convertir de °C a °F
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5. Función check-season que devuelve la estación según el mes
def check_season(month):
    seasons = {
        "Winter": [12, 1, 2],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11]
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Mes no válido"

# 6. Función para calcular la pendiente de una ecuación lineal
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pendiente es indefinida (división por cero)"
    return (y2 - y1) / (x2 - x1)

# 7. Función para resolver una ecuación cuadrática
import math
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return "No hay soluciones reales"

# 8. Función para imprimir una lista
def print_list(lst):
    for item in lst:
        print(item)

# 9. Función para invertir una lista usando bucles
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 10. Función para capitalizar los elementos de una lista
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11. Función para añadir un ítem al final de una lista
def add_item(lst, item):
    lst.append(item)
    return lst

# 12. Función para eliminar un ítem de una lista
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Función para calcular la suma de los números en un rango
def sum_of_numbers(n):
    return sum(range(1, n+1))

# 14. Función para sumar los números impares en un rango
def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)

# 15. Función para sumar los números pares en un rango
def sum_of_even(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)
