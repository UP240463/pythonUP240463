# Dia 11

# Nivel 2

# 1. Función para contar números pares e impares en un número
def evens_and_odds(num):
    evens = sum(1 for digit in str(num) if int(digit) % 2 == 0)
    odds = len(str(num)) - evens
    return f"The number of evens are {evens}. The number of odds are {odds}."

# 2. Función para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 3. Función para verificar si algo está vacío
def is_empty(value):
    return len(value) == 0 if isinstance(value, (str, list, dict)) else value == 0

# 4. Funciones para calcular la media, mediana, moda, rango, varianza y desviación estándar de una lista
import statistics

def calculate_mean(lst):
    return statistics.mean(lst)

def calculate_median(lst):
    return statistics.median(lst)

def calculate_mode(lst):
    return statistics.mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return statistics.variance(lst)

def calculate_std(lst):
    return statistics.stdev(lst)
