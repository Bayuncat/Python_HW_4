# Использовал 2 решения, поскольку точность предполагает округление, а в примере решения значение обрезается

import math

a = float(input("Задайте требуемую точность вывода числа Pi от 0.0 до 0.0000000000000001: "))

b = 0
while a < 1:
    a = a*10
    b +=1

print("Решение 1 используя округление:")
print(round(math.pi, b))

print("Решение 2 обрезаем ненужное количество цифр:")
print(str(math.pi)[0:2+b])

