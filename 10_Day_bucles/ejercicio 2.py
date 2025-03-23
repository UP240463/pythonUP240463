# Dia 10

# Nivel 2

# 1. Sumar todos los números del 0 al 100:
total = 0
for i in range(101):
    total += i
print(f"\nLa suma de todos los números es {total}")

# 2. Sumar todos los números pares y todos los números impares del 0 al 100:
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"\nLa suma de todos los números pares es {even_sum}. Y la suma de todos los impares es {odd_sum}.")