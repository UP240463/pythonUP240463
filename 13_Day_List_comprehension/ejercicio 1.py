
# Day 13

# 1. Filtrar solo números negativos y cero usando list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print("Números negativos y cero:", filtered_numbers)

# 2. Aplanar la lista de listas de listas en una lista unidimensional
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for inner in sublist for item in inner]
print("Lista aplanada:", flattened_list)

# 3. Crear la lista de tuplas usando list comprehension
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("Lista de tuplas:")
for t in list_of_tuples:
    print(t)

# 4. Aplanar la lista de países y ciudades con formato
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0].upper(), country[0][:3].upper(), city[0].upper()] for country, city in countries]
print("Lista de países y ciudades formateada:", flattened_countries)

# 5. Cambiar la lista de listas a una lista de diccionarios
dict_countries = [{'country': country[0][0].upper(), 'city': city[0][1].upper()} for country, city in countries]
print("Lista de diccionarios:", dict_countries)

# 6. Cambiar la lista de listas a una lista de cadenas concatenadas
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{name[0][0]} {name[0][1]}" for name in names]
print("Lista de nombres concatenados:", concatenated_names)

# 7. Función lambda para calcular pendiente y ordenada al origen (y-intercepto)
slope_intercept = lambda x1, y1, x2, y2: (
    ((y2 - y1) / (x2 - x1) if x2 != x1 else None),  # Slope
    y1 - ((y2 - y1) / (x2 - x1)) * x1 if x2 != x1 else None  # Y-intercept
)

# Ejemplo: Calcular la pendiente y el intercepto para los puntos (1, 2) y (3, 6)
m, b = slope_intercept(1, 2, 3, 6)
print(f"\nPendiente: {m}, Intercepto en Y: {b}")
