 # dia 9

#1.Calificar a los estudiantes según sus puntuaciones:

puntuacion = int(input("Ingresa tu puntuación: "))

if 80 <= puntuacion <= 100:
    print("A")
elif 70 <= puntuacion <= 89:
    print("B")
elif 60 <= puntuacion <= 69:
    print("C")
elif 50 <= puntuacion <= 59:
    print("D")
else:
    print("F")

#2.Comprobar la temporada según el mes:

mes = input("Ingresa un mes: ").lower()

if mes in ['septiembre', 'octubre', 'noviembre']:
    print("Es otoño.")
elif mes in ['diciembre', 'enero', 'febrero']:
    print("Es invierno.")
elif mes in ['marzo', 'abril', 'mayo']:
    print("Es primavera.")
elif mes in ['junio', 'julio', 'agosto']:
    print("Es verano.")
else:
    print("Mes no válido.")
    
#3.Añadir frutas a una lista:

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Ingresa una fruta: ").lower()

if fruit in fruits:
    print("Esa fruta ya existe en la lista.")
else:
    fruits.append(fruit)
    print("Lista modificada:", fruits)