# ДЗ на вторник:

#1. # 1. Создать с помощью матрицы таблицу умножения с корректным выводом на экран.
# Дополнительно можно добавить сетку из символов | —, которая будет отделять числа.
#1. Решение 1
# Matrix = [[1]*10 for i in range(1, 11)]
# for i in range(1, 11):
#     for j in range(1, 11):
#         Matrix[i-1][j-1] = i*j
# for i in range(len(Matrix)):
#     for j in range(len(Matrix[i])):
#         print(f'{i+1} * {j+1} = {Matrix[i][j]}', end=' | ')
#     print()

#1. Решение 2
# Matrix = [[i]*10 for i in range(1, 11)]
# # print(Matrix)
# for i in range(1, 11):
#     for j in range(1, 11):
#         Matrix[i-1][j-1] = i*j
# print('Х || 1   2   3   4   5   6   7   8   9   10')
# for i in range(len(Matrix)):
#     print(i+1, end=' || ')
#     for j in range(len(Matrix[i])):
#         print(f'{Matrix[i][j]}', end=' | ')
#     print()

# 2. Напишите код с конструкцией try-except-finally с наглядной демонстрацией, зачем использовать finally,
# если можно просто написать код после конструкции try-except
# Задание присылать в формате Иванов.Lesson_7

# cveta = {1: 'Красный', 2: 'Жёлтый', 3: 'Зелёный'}
# try:
#     i = int(input('Введите цифрой цвет светофора (1 - Красный, 2 - Жёлтый, 3 - Зелёный): '))
# except ValueError:
#     print('Вы ввели не число!')
# else:
#     if i in cveta:
#         print(cveta[i])
#     else: print('Такого значения нет!')
# finally: print('Выход без ошибок')