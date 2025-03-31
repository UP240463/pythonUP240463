
# Day 14

from functools import reduce

# Datos de ejemplo
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Nivel 1

# 1. Diferencia entre map, filter y reduce
# map: Aplica una función a cada elemento
upper_countries = list(map(lambda x: x.upper(), countries))
print("Countries in uppercase:", upper_countries)

# filter: Filtra los elementos según una condición
countries_with_land = list(filter(lambda x: 'land' in x.lower(), countries))
print("Countries containing 'land':", countries_with_land)

# reduce: Reduce los elementos de una lista a un único valor
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

# 2. Funciones de orden superior, closure y decoradores
# Higher-order function
def higher_order_func(func):
    return func(5)

def square(x):
    return x ** 2

print("Higher-order function result:", higher_order_func(square))

# Closure
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

add_5 = outer_func(5)
print("Closure result:", add_5(10))

# Decorator
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()

# 3. Funciones de llamada antes de map, filter o reduce
def square(x):
    return x ** 2

numbers_squared = list(map(square, numbers))
print("Numbers squared using map:", numbers_squared)

# 4. Uso de for loop para imprimir países, nombres y números

print("Countries:")
for country in countries:
    print(country)

print("Names:")
for name in names:
    print(name)

print("Numbers:")
for number in numbers:
    print(number)


# Nivel 2

# 1. map para cambiar cada país a mayúsculas
countries_upper = list(map(lambda x: x.upper(), countries))
print("Countries in uppercase using map:", countries_upper)

# 2. map para cambiar cada número a su cuadrado
numbers_squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers using map:", numbers_squared)

# 3. map para cambiar cada nombre a mayúsculas
names_upper = list(map(lambda x: x.upper(), names))
print("Names in uppercase using map:", names_upper)

# 4. filter para filtrar países que contienen 'land'
countries_with_land = list(filter(lambda x: 'land' in x.lower(), countries))
print("Countries containing 'land' using filter:", countries_with_land)

# 5. filter para filtrar países con exactamente seis caracteres
countries_with_six_chars = list(filter(lambda x: len(x) == 6, countries))
print("Countries with exactly 6 characters using filter:", countries_with_six_chars)

# 6. filter para filtrar países con más de seis letras
countries_more_than_six_chars = list(filter(lambda x: len(x) > 6, countries))
print("Countries with more than 6 characters using filter:", countries_more_than_six_chars)

# 7. filter para filtrar países que comienzan con 'E'
countries_starting_with_e = list(filter(lambda x: x.startswith('E'), countries))
print("Countries starting with 'E' using filter:", countries_starting_with_e)

# 8. Cadena de iteradores (map -> filter -> reduce)
result = reduce(lambda x, y: x + y, 
                list(filter(lambda x: len(x) > 6, 
                list(map(lambda x: x.upper(), countries)))))
print("Chained result (map -> filter -> reduce):", result)

# 9. Función que devuelve solo elementos string de una lista
def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]

mixed_list = [1, 'hello', 3.14, 'world', True]
string_items = get_string_lists(mixed_list)
print("String items in mixed list:", string_items)

# 10. Reduce para sumar todos los números de la lista
sum_all_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of all numbers using reduce:", sum_all_numbers)

# 11. Reduce para concatenar todos los países en una oración
countries_sentence = reduce(lambda x, y: x + ', ' + y, countries)
countries_sentence += " are north European countries"
print("Countries sentence using reduce:", countries_sentence)

# 12. Función para categorizar países con patrones comunes
def categorize_countries():
    patterns = ['land', 'ia', 'island', 'stan']
    categorized = {pattern: [] for pattern in patterns}
    for country in countries:
        for pattern in patterns:
            if pattern in country.lower():
                categorized[pattern].append(country)
    return categorized

categorized_countries = categorize_countries()
print("Categorized countries by patterns:", categorized_countries)

# 13. Diccionario con letras iniciales y la cantidad de países
def country_initials_dict():
    initials = {}
    for country in countries:
        first_letter = country[0].upper()
        initials[first_letter] = initials.get(first_letter, 0) + 1
    return initials

initials_dict = country_initials_dict()
print("Initials dictionary:", initials_dict)

# 14. Obtener los primeros diez países de la lista
def get_first_ten_countries():
    return countries[:10]

first_ten_countries = get_first_ten_countries()
print("First ten countries:", first_ten_countries)

# 15. Obtener los últimos diez países de la lista
def get_last_ten_countries():
    return countries[-10:]

last_ten_countries = get_last_ten_countries()
print("Last ten countries:", last_ten_countries)
