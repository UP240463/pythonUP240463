
# Day 18

import re
from collections import Counter

# Ejercicio Nivel 2 - 1: Validación de nombre de variable válido en Python
def is_valid_variable(variable):
    return bool(re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', variable))

# Probar con algunos ejemplos
print("Ejercicio 3: Validación de nombres de variables válidos")
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True
print()