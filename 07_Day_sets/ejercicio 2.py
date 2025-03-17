# dia 7


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


#1.Unir A y B
c = B.union(A)
print(c)

#2.Encuentra la intersección de A y B
print(A.intersection(B))

#3.Es un subconjunto de B
print(A.issubset(B))

#4.¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B))

#5.Unir A con B y B con A
print(B.union(A))
print(A.union(B))

#6.Unir A con B y B con A
print(A.symmetric_difference(B))

#7.Eliminar los conjuntos por completo
del A
del B