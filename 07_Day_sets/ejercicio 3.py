# dia 7

age = [22, 19, 24, 25, 26, 24, 25, 24]

#1.Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
st = set(age)
print(len(st))
print(len(age))

#2. Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto.

#La diferencia es que los tipo string, es un tipo de variable que nos sirve para almacenar
#caracteres, las listas, para almacenar varios caracteres dentro de una sola variable, los 
#tuple, es de misma forma una lista pero no nos permite modificarla, y los sets
#de misma forma son una manera de almacenar datos, con la diferencia de que estos no nos permiten
#repetir los mismos. 

#3.Soy profesor y me encanta inspirar y enseñar.
# ¿Cuántas palabras únicas se han usado en la oración? Usa los métodos de división y configuración para obtener las palabras únicas.
sentence = "I am a teacher and I love to inspire and teach people"
word = set(sentence.split())
print(len(word))