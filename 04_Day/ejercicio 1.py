# 1. Concatenar las cadenas 'Thirty', 'Days', 'Of', 'Python' en una sola cadena
cadena_concatenada = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print("Cadena concatenada:", cadena_concatenada)

# 2. Concatenar las cadenas 'Coding', 'For', 'All' en una sola cadena
cadena_concatenada_2 = 'Coding ' + 'For ' + 'All'
print("Cadena concatenada:", cadena_concatenada_2)

# 3. Declarar una variable llamada company y asignarle el valor "Coding For All"
company = "Coding For All"

# 4. Imprimir la variable company
print("Company:", company)

# 5. Imprimir la longitud de la cadena company
print("Longitud de la cadena company:", len(company))

# 6. Cambiar todos los caracteres a mayúsculas
print("Cadena en mayúsculas:", company.upper())

# 7. Cambiar todos los caracteres a minúsculas
print("Cadena en minúsculas:", company.lower())

# 8. Usar capitalize(), title(), swapcase() para formatear la cadena
print("Capitalize:", company.capitalize())
print("Title:", company.title())
print("Swapcase:", company.swapcase())

# 9. Cortar (slice) la primera palabra de la cadena
primera_palabra = company.split()[0]
print("Primera palabra:", primera_palabra)

# 10. Verificar si la cadena contiene la palabra 'Coding'
print("¿Contiene 'Coding'?:", "Coding" in company)

# 11. Reemplazar 'Coding' por 'Python' en la cadena
cadena_reemplazada = company.replace("Coding", "Python")
print("Cadena reemplazada:", cadena_reemplazada)

# 12. Cambiar 'Python for Everyone' a 'Python for All'
cadena_cambiada = "Python for Everyone".replace("Everyone", "All")
print("Cadena cambiada:", cadena_cambiada)

# 13. Dividir la cadena 'Coding For All' usando espacio como separador
print("Cadena dividida:", company.split())

# 14. Dividir la cadena "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" en la coma
cadena_empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("Cadena dividida en comas:", cadena_empresas.split(", "))

# 15. Carácter en el índice 0 de la cadena 'Coding For All'
print("Carácter en índice 0:", company[0])

# 16. Último índice de la cadena 'Coding For All'
print("Último índice:", len(company) - 1)

# 17. Carácter en el índice 10 de la cadena 'Coding For All'
print("Carácter en índice 10:", company[10])

# 18. Crear un acrónimo para 'Python For Everyone'
acronimo_pfe = ''.join([palabra[0] for palabra in "Python For Everyone".split()])
print("Acrónimo de 'Python For Everyone':", acronimo_pfe)

# 19. Crear un acrónimo para 'Coding For All'
acronimo_cfa = ''.join([palabra[0] for palabra in "Coding For All".split()])
print("Acrónimo de 'Coding For All':", acronimo_cfa)

# 20. Posición de la primera ocurrencia de 'C' en 'Coding For All'
print("Primera ocurrencia de 'C':", company.find('C'))

# 21. Posición de la primera ocurrencia de 'F' en 'Coding For All'
print("Primera ocurrencia de 'F':", company.find('F'))

# 22. Posición de la última ocurrencia de 'l' en 'Coding For All People'
cadena_larga = "Coding For All People"
print("Última ocurrencia de 'l':", cadena_larga.rfind('l'))

# 23. Posición de la primera ocurrencia de 'because' en la oración
oracion = 'You cannot end a sentence with because because because is a conjunction'
print("Primera ocurrencia de 'because':", oracion.find('because'))

# 24. Posición de la última ocurrencia de 'because' en la oración
print("Última ocurrencia de 'because':", oracion.rindex('because'))

# 25. Extraer la frase 'because because because' de la oración
frase_extraida = oracion[31:54]
print("Frase extraída:", frase_extraida)

# 26. Verificar si 'Coding For All' comienza con 'Coding'
print("¿Comienza con 'Coding'?:", company.startswith('Coding'))

# 27. Verificar si 'Coding For All' termina con 'coding'
print("¿Termina con 'coding'?:", company.endswith('coding'))

# 28. Eliminar espacios al principio y al final de '   Coding For All      '
cadena_espacios = '   Coding For All      '
print("Cadena sin espacios:", cadena_espacios.strip())

# 29. Verificar si las siguientes variables son identificadores válidos
print("¿'30DaysOfPython' es identificador?:", '30DaysOfPython'.isidentifier())
print("¿'thirty_days_of_python' es identificador?:", 'thirty_days_of_python'.isidentifier())

# 30. Unir la lista de bibliotecas con un hash y espacio
bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("Bibliotecas unidas:", '# '.join(bibliotecas))

# 31. Usar secuencia de escape de nueva línea para separar oraciones
print("I am enjoying this challenge.\nI just wonder what is next.")

# 32. Usar secuencia de escape de tabulación para formatear
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 33. Calcular el área de un círculo y formatear la salida
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 34. Formatear operaciones matemáticas
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")