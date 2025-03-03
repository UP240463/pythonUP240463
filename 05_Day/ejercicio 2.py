# Lista de edades de 10 estudiantes
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Ordenar la lista y encontrar la edad mínima y máxima
edades.sort()
edad_minima = min(edades)
edad_maxima = max(edades)
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

# 2. Agregar la edad mínima y máxima nuevamente a la lista
edades.append(edad_minima)
edades.append(edad_maxima)
print("Edades después de agregar mínima y máxima:", edades)

# 3. Encontrar la mediana de las edades
longitud_edades = len(edades)
if longitud_edades % 2 == 0:
    mediana = (edades[longitud_edades // 2 - 1] + edades[longitud_edades // 2]) / 2
else:
    mediana = edades[longitud_edades // 2]
print("Mediana de las edades:", mediana)

# 4. Encontrar la edad promedio
promedio_edades = sum(edades) / len(edades)
print("Edad promedio:", promedio_edades)

# 5. Encontrar el rango de las edades (máximo - mínimo)
rango_edades = edad_maxima - edad_minima
print("Rango de las edades:", rango_edades)

# 6. Comparar los valores de (mínimo - promedio) y (máximo - promedio) usando abs()
diferencia_min = abs(edad_minima - promedio_edades)
diferencia_max = abs(edad_maxima - promedio_edades)
print("Diferencia entre mínima y promedio:", diferencia_min)
print("Diferencia entre máxima y promedio:", diferencia_max)

# 7. Encontrar el/los país(es) del medio en la lista de países
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
longitud_paises = len(paises)
if longitud_paises % 2 == 0:
    paises_medios = paises[longitud_paises // 2 - 1:longitud_paises // 2 + 1]
else:
    paises_medios = [paises[longitud_paises // 2]]
print("País(es) del medio:", paises_medios)

# 8. Dividir la lista de países en dos listas iguales (o una más grande si es impar)
mitad = (longitud_paises + 1) // 2  # Asegura que la primera mitad sea más grande si es impar
primera_mitad = paises[:mitad]
segunda_mitad = paises[mitad:]
print("Primera mitad de países:", primera_mitad)
print("Segunda mitad de países:", segunda_mitad)

# 9. Desempaquetar los primeros tres países y el resto como países escandinavos
primeros_tres, *paises_escandinavos = paises
print("Primeros tres países:", primeros_tres)
print("Países escandinavos:", paises_escandinavos)