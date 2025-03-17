# dia 9

#1. Obtener la edad del usuario e indicar si tiene edad suficiente para conducir:
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Tiene edad suficiente para conducir.")
else:
    print(f"Espere {18 - edad} años para poder conducir.")
    

#2.Comparar las edades de dos personas (my_age y your_age):
my_age = 25  # Tu edad (puedes cambiarla según prefieras)
your_age = int(input("Ingresa tu edad: "))

if my_age > your_age:
    if my_age - your_age == 1:
        print(f"Tengo 1 año más que tú.")
    else:
        print(f"Tengo {my_age - your_age} años más que tú.")
elif my_age < your_age:
    if your_age - my_age == 1:
        print(f"Tienes 1 año más que yo.")
    else:
        print(f"Tienes {your_age - my_age} años más que yo.")
else:
    print("Tenemos la misma edad.")


#3.Obtener dos números e indicar cuál es mayor, menor o si son iguales:
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")



