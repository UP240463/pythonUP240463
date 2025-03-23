# Dia 11

# Nivel 3

# 1. Función para verificar si un número es primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 2. Función para verificar si todos los ítems de una lista son únicos
def all_items_unique(lst):
    return len(lst) == len(set(lst))

# 3. Función para verificar si todos los ítems de la lista son del mismo tipo de dato
def all_items_same_type(lst):
    return len(set(type(item) for item in lst)) == 1

# 4. Función para verificar si una variable es un nombre de variable válido en Python
def is_valid_python_variable(var_name):
    return var_name.isidentifier() and not var_name.isdigit()

# 5. Función para obtener los 10 o 20 idiomas más hablados en el mundo (asumimos datos)
def most_spoken_languages():
    languages = {
        "Mandarin": 1117, "Spanish": 460, "English": 379, "Hindi": 341, "Arabic": 315,
        "Bengali": 230, "Portuguese": 221, "Russian": 154, "Japanese": 128, "Lahnda (Punjabi)": 118
    }
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]

# 6. Función para obtener los 10 o 20 países más poblados del mundo (asumimos datos)
def most_populated_countries():
    countries = {
        "China": 1393409038, "India": 1366417754, "USA": 331002651, "Indonesia": 273523615, "Pakistan": 220892340,
        "Brazil": 212559417, "Nigeria": 206139589, "Bangladesh": 164689383, "Russia": 145934462, "Mexico": 128933395
    }
    return sorted(countries.items(), key=lambda x: x[1], reverse=True)[:10]