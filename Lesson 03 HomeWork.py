# ДЗ на четверг:
# Создать список a = [1,2,3,4,5,6,7,8,9,10] с помощью генерации списка, используя range,
# либо список случайных чисел и случайной длины.
# Получить список b, состоящий из элементов списка a, возведенных в квадрат (x*x)
# Файл прислать в личку в формате Ivanov.Lesson_3.py

# import random
# from random import randint
# a = []
# a2 = []
# b = []
# b2 = []
# for i in range(1, 11):
#     a.append(i)
#     b.append(i*i)
# print('Список a: ', a)
# print('Список b: ', b)
# a2 = [randint(0, j) for j in range(randint(1, 100))]
# print('Список а2: ', a2)
# for i in a2:
#     b2.append(i*i)
# print('Список b2: ', b2)

input_string = 'eefeeeeefff'
print(input_string.split('e', 2))

