import random
'''
Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''

size = int(input("Введите размер массива "))
list = []
for i in range(size):
    list.append(random.randint(-15, 15))
print(*list)

num = int(input("Введите число "))
best_num = list[0]

for i in list:
    if abs(num-i) < abs(num-best_num):
        best_num = i


print(best_num)
