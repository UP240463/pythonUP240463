# dia 8

# 1. Crear un diccionario vacío llamado perro
perro = {}

# 2. Añadir nombre, color, raza, patas y edad al diccionario de perros
perro['nombre'] = 'Firulais'
perro['color'] = 'marrón'
perro['raza'] = 'Labrador'
perro['patas'] = 4
perro['edad'] = 3

# 3. Crear un diccionario de estudiantes con diversas claves
estudiante = {
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'género': 'Masculino',
    'edad': 21,
    'estado civil': 'Soltero',
    'habilidades': ['programación', 'matemáticas'],
    'país': 'México',
    'ciudad': 'Ciudad de México',
    'dirección': 'Calle Ficticia 123'
}

# 4. Obtener la longitud del diccionario del estudiante
longitud_estudiante = len(estudiante)
print("Longitud del diccionario del estudiante:", longitud_estudiante)

# 5. Obtener el valor de las habilidades y verificar su tipo de dato
habilidades = estudiante['habilidades']
print("Habilidades:", habilidades)
print("Tipo de dato de habilidades:", type(habilidades))

# 6. Modificar los valores de las habilidades agregando una o dos habilidades
estudiante['habilidades'].append('diseño gráfico')
estudiante['habilidades'].append('gestión de proyectos')
print("Habilidades modificadas:", estudiante['habilidades'])

# 7. Obtener las claves del diccionario como una lista
claves_estudiante = list(estudiante.keys())
print("Claves del diccionario:", claves_estudiante)

# 8. Obtener los valores del diccionario como una lista
valores_estudiante = list(estudiante.values())
print("Valores del diccionario:", valores_estudiante)

# 9. Cambiar el diccionario a una lista de tuplas usando el método items()
tuplas_estudiante = list(estudiante.items())
print("Diccionario convertido en lista de tuplas:", tuplas_estudiante)

# 10. Eliminar uno de los elementos del diccionario
del estudiante['dirección']
print("Diccionario después de eliminar la dirección:", estudiante)

# 11. Eliminar el diccionario completo
del estudiante
print("Diccionario de estudiante eliminado:", estudiante)  # Esto generará un error porque el diccionario ha sido eliminado
