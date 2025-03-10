
# dia 6

print(" DAY 6 in python")

# ejercicio 1

h = ['luis']
m =['paola','monica']
print("hermanos en total:")
hermanos = h+m
print(hermanos)
padres = ['jose','maria']
print("familia total:")
familia = hermanos +  padres
print(familia)

#ejercicio 2
famlia = ("jose","maria","paola","monica","luis")
jose, maria, *hermanos = familia

#creamos tuplas de frutas vegetales y productos animales
frutas = ['manzan','pera','fresa']
verduras = ['brocoli','jitomate','nopal']
pdanimales = ['crema','queso','leche']
food_stuff_tp = frutas+verduras+pdanimales
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index] if len(food_stuff_lt) % 2 != 0 else food_stuff_lt[middle_index - 1:middle_index + 1]
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print(is_estonia_nordic)  # Output: False

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print(is_iceland_nordic)  # Output: True



