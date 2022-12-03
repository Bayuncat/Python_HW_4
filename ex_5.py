import sympy
from sympy import *

x = sympy.Symbol('x')
read_file1 = open('coef_1.txt','r')
read_file2 = open('coef_2.txt','r')

coefficient1 = read_file1.readline().split(',')
coefficient2 = read_file2.readline().split(',')

read_file1.close()
read_file2.close()

p1 = list(map(int, coefficient1))
p2 = list(map(int, coefficient2))

poly1 = sum(coef*x**i for i, coef in enumerate(reversed(p1)))
poly2 = sum(coef*x**i for i, coef in enumerate(reversed(p2)))

print(f'Полином 1: {poly1} = 0')
print(f'Полином 1: {poly2} = 0')

print(f'итоговый полином: {simplify(poly1+poly2)} = 0')