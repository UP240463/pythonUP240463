# Dia 12

# Nivel 1

#Generar un ID de usuario aleatorio de 6 caracteres.
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
# Ejemplo de uso:
print(random_user_id())  # Salida: '1ee33d' (puede variar)


#Generar múltiples IDs de usuario según el input del usuario.
def user_id_gen_by_user():
    num_chars = int(input("Ingresa el número de caracteres para el ID: "))
    num_ids = int(input("Ingresa el número de IDs a generar: "))
    ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        ids.append(user_id)
    return '\n'.join(ids)
# Ejemplo de uso:
# Entrada del usuario: 5 5
print(user_id_gen_by_user())  # Salida: una lista de 5 IDs generados


#Generar un color RGB aleatorio.
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

# Ejemplo de uso:
print(rgb_color_gen())  # Salida: 'rgb(125,244,255)' (puede variar)