# Dia 12

# Nivel 2

# una lista de colores hexadecimales.
def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        hex_color = f'#{random.randint(0, 0xFFFFFF):06x}'
        hex_colors.append(hex_color)
    return hex_colors

# Ejemplo de uso:
print(list_of_hexa_colors(5))  # Salida: ['#a3e12f', '#03ed55', '#eb3d2b', '#b334ef', '#F0A2B5']


#Generar una lista de colores RGB.
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f'rgb({r},{g},{b})')
    return rgb_colors

# Ejemplo de uso:
print(list_of_rgb_colors(5))  # Salida: ['rgb(5, 55, 175)', 'rgb(50, 105, 100)', 'rgb(15, 26, 80)', 'rgb(33,79, 176)']


#Generar colores hexadecimales o RGB basados en un tipo de entrada.
def generate_colors(color_type, num_colors):
    colors = []
    if color_type == 'hexa':
        for _ in range(num_colors):
            hex_color = f'#{random.randint(0, 0xFFFFFF):06x}'
            colors.append(hex_color)
    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f'rgb({r},{g},{b})')
    return colors

# Ejemplo de uso:
print(generate_colors('hexa', 3))  # Salida: ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('rgb', 1))   # Salida: ['rgb(33,79,176)']
