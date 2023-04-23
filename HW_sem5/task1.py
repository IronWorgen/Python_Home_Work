'''
Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
'''

# Функция возвразает список, где первый элемент - это факториал числа N, а второй - это треугольное число.


def fact_and_sum(num):
    if (num == 1):
        return [1, 1]

    list = [num, num]
    return [list[0]*fact_and_sum(num-1)[0], list[1]+fact_and_sum(num-1)[1]]


print(fact_and_sum(6))
