a = list()
num1 = int(input("введите первый элемент: "))
d = int(input("введите разность прогрессии: "))
n = int(input("введите колличество элементов: "))
for i in range(n):
    a.append(num1+i*d)
print (a)