#   Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Введите число: "))
result = ""
for i in range(num):
    pow2 = 2**i
    if (pow2>=num):
        break
    result += str(pow2)+", "
print(result[:-2])