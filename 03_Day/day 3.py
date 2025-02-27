# ejercicio 1

# operadores 

age = int(18) 
height = 1.82
comp = 7j
print(age)
print(height)
print(comp)
#--------------------------
b = int(input('base = '))
h = int(input('height = '))
print('The area is = ', 0.5*b*h)
side_a = int(input('Side a = '))
side_b = int(input('Side b = '))
side_c = int(input('Side c = '))
perimeter = side_a + side_b + side_c
print('The perimeter equals', perimeter)
#----------------------------------------
length = int(input('length = '))
width = int(input('width = '))
area_rec, perimeter_rec = width*length, 2*(length + width)
print('area is', area_rec, 'perimeter is', perimeter_rec)
#---------------------------------------------
radius = int(input('radius= '))
pi = 3.14
area_circ, circum = pi*radius**2, 2*pi*radius
print('area is', area_circ, 'circumference is', circum)
#-------------------------------------------
x = int(input('x= '))
slope = (2*x)-2
print(slope)
#---------------------------------------------
slope1 = (10-2)/(6-2)
print(slope1)
#---------------------------------------------
x = int(input('x= '))
y = (x**2)+(6*x)+9
print(y)
#------------------------------------------------
print(len('python') < len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'i hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')
print(len('python'))
print(float(len('python')))
print(str(len('python')))
#-------------------------------------------------------
num = int(input ('Enter any number: ')) 
if((num % 2) == 0): print('even') 
else: print('The provided number is odd')
#-------------------------------------------
print(7//3 == 2.7)
print('10' == 10)
print(9.8 == 10)
#------------------------------------------
hrs = int(input('hours: '))
rate = int(input('rate: '))
pay = hrs * rate 
print('payment: ',pay)
#---------------------------------------------
years = int(input('Number of years: '))
seconds = years*3600 
print('youve lived for: ', seconds)
#------------------------------------------
for i in range(1,6):
    print(f'{i} {i**0} {i**2} {i**3}')
    