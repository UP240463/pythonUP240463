# day 7

#sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1.Encuentra la longitud del conjunto it_companies
print(len(it_companies))

#2.Añade 'Twitter' a it_companies
it_companies.add('Twitter')
print(it_companies)

#3.Insertar varias empresas de TI a la vez en el conjunto it_companies
it_companies.update(['X', 'Steam', 'Instagram'])
print(it_companies)

#4.Insertar varias empresas de TI a la vez en el conjunto it_companies
it_companies.remove('Twitter')
print(it_companies)

#5.¿Cuál es la diferencia entre eliminar y descartar?
#Usar descartar, si el item no existe, no se tiene error, caso cotnrario de lo que pasa con remove. 
it_companies.discard('OLA')
print(it_companies)
