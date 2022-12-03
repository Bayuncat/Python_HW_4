import sympy 
from random import randint

x = sympy.Symbol('x')

a = int(input("Введите натуральное число степени: "))
coefficients=[]

for i in range(0,a+1):
    coefficients.append(randint(0, 100))

p1 = sum(coef*x**i for i, coef in enumerate(reversed(coefficients)))

print(f'{p1} = 0')

f = open('ex4poly.txt','w')
f.write(str(p1)+' = 0')
f.close() 