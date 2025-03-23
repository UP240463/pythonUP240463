# Dia 12

# Nivel 3

#Barajar una lista.
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# Ejemplo de uso:
print(shuffle_list([1, 2, 3, 4, 5]))  # Salida: [4, 1, 3, 5, 2] (puede variar)


#Generar una lista de 7 números aleatorios únicos entre 0 y 9.
def unique_random_numbers():
    return random.sample(range(10), 7)

# Ejemplo de uso:
print(unique_random_numbers())  # Salida: [9, 1, 5, 3, 7, 2, 8] (puede variar)