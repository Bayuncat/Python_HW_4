a = int(input("Введите натуральное число для вывода его простых множетелей: "))
dev=[]

for i in range(1, a+1):
    c = a % i
    if c == 0: dev.append(i)

print(f'Список множетелей числа {a}: {dev}')

lst = [1]
for i in range(1, len(dev)):
    for j in range(2, dev[i]):
        if dev[i] % j == 0: break
    else:
        lst.append(dev[i])
print(f'Список простых множетелей числа {a}: {lst}')
