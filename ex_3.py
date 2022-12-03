from random import randint

def Filist():
    length=randint(5, 10)
    yourlist = [randint(0, 10) for i in range(length)]
    return(yourlist)

mylist=Filist() + Filist()
print(f'Задана последовательность чисел: {mylist}')

res = [x for x in mylist if mylist.count(x) == 1]

print(f'Неповторяющиеся чиcла в данной последовательности: {res}')