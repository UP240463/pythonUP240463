
# Day 18

import re
from collections import Counter

# Ejercicio Nivel 3 - 1: Limpiar el texto y contar las tres palabras más frecuentes
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Limpiar el texto eliminando caracteres no deseados
cleaned_text = re.sub(r'[^\w\s]', '', sentence)  # Eliminar caracteres especiales

# Contar las palabras más frecuentes
words = re.findall(r'\b\w+\b', cleaned_text.lower())
word_count = Counter(words)

print("Ejercicio 4: Tres palabras más frecuentes")
print(word_count.most_common(3))