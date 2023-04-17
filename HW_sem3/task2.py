import random
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
