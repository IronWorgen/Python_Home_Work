import random
arr = list()
for i in range(int(input("Размер массива: "))):
    arr.append(random.randint(1, 20))
print(arr)
min_num = int(input("минимальное значение: "))
max_num = int(input("максимальное  значение: "))
result = list()
for i in range(len(arr)):
    if arr[i] >= min_num and arr[i] <= max_num:
        result.append(arr[i])
result.sort()
print(result)
