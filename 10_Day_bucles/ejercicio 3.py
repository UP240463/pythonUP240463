# Dia 1o

# Nivel 3

# 1. Extraer todos los países que contienen la palabra "land" (suponiendo que tienes el archivo countries.py):
# Aquí se asume que el archivo `countries.py` tiene una lista de países.
# from countries import countries  # Importar la lista de países desde el archivo

# Simulando una lista de países
countries = ['Finland', 'Iceland', 'Ireland', 'Poland', 'Switzerland', 'Thailand', 'Denmark']
land_countries = [country for country in countries if "land" in country.lower()]
print("\nPaíses que contienen 'land':", land_countries)

# 2. Invertir el orden de la lista de frutas usando un bucle:
fruits = ['banana', 'orange', 'mango', 'lemon']
print("\nFrutas en orden inverso:")
for fruit in reversed(fruits):
    print(fruit)

# 3. Calcular el número total de lenguajes en un archivo de datos (suponiendo que tienes el archivo countries_data.py):
# Aquí se asume que el archivo `countries_data.py` tiene información estructurada sobre países.

# Simulando datos de países con lenguas
data = [
    {'name': 'Finland', 'languages': ['Finnish', 'Swedish']},
    {'name': 'Iceland', 'languages': ['Icelandic']},
    {'name': 'Ireland', 'languages': ['Irish', 'English']},
    {'name': 'Poland', 'languages': ['Polish']},
    {'name': 'Switzerland', 'languages': ['German', 'French', 'Italian', 'Romansh']}
]

total_languages = 0
for country in data:
    total_languages += len(country['languages'])
print(f"\nEl número total de lenguajes es {total_languages}")

# 4. Encontrar los 10 lenguajes más hablados (suponiendo que tienes el archivo countries_data.py):
from collections import Counter

languages = []
for country in data:
    languages.extend(country['languages'])
language_count = Counter(languages)
most_common_languages = language_count.most_common(10)
print("\nLos 10 lenguajes más hablados son:", most_common_languages)

# 5. Encontrar los 10 países más poblados (suponiendo que tienes el archivo countries_data.py):
# Añadiendo población a los datos simulados
data = [
    {'name': 'Finland', 'population': 5500000, 'languages': ['Finnish', 'Swedish']},
    {'name': 'Iceland', 'population': 360000, 'languages': ['Icelandic']},
    {'name': 'Ireland', 'population': 4900000, 'languages': ['Irish', 'English']},
    {'name': 'Poland', 'population': 38000000, 'languages': ['Polish']},
    {'name': 'Switzerland', 'population': 8500000, 'languages': ['German', 'French', 'Italian', 'Romansh']},
    {'name': 'China', 'population': 1393409038, 'languages': ['Mandarin']},
    {'name': 'India', 'population': 1366417754, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 331002651, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 273523615, 'languages': ['Indonesian']},
    {'name': 'Brazil', 'population': 212559417, 'languages': ['Portuguese']}
]

# Ordenar países por población y obtener los 10 más poblados
sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
top_10_populated = sorted_countries[:10]
print("\nLos 10 países más poblados son:")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']}")
