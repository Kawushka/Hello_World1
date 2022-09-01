# ДЗ на четверг:
# ДЗ оформляем как Иванов.Lesson_6.py

# 1. На входе пользователь вводит несколько чисел через пробел. На выходе - количество чисел,
# которые не повторяются.
#
# a = input('Введите числа через пробел: ').split() #split превратит строку в список. По умолчанию разбивает по пробелам
# print(a)
# b = []
# for i in a:
#     if a.count(i)==1: b.append(int(i))
# print(b)
# print(len(b))


# 2. На входе пользователь дважды вводит несколько чисел через пробел.
# На выходе - количество чисел, которые содержатся одновременно в первом и втором списке.

# print(len(set(input('Введите числа через пробел: ').split())&set(input('Введите числа через пробел: ').split())))

# 3. На входе пользователь дважды вводит несколько чисел через пробел.
# На выходе - вывести совпадающие числа в порядке возрастания

# print(*sorted(set(input('Введите числа: ').split()) & set(input('Введите числа: ').split())))



# 4. (Дополнительно) На входе пользователь вводит несколько чисел через пробел.
# На выходе - вывести все числа в столбик, напротив каждого написать слово "Встречалось" или "Не встречалось", если число уже было в последовательности.

# chislo = input('Введите числа: ').split()
# chislo_2 = []
# for i in chislo:
#     if chislo_2.count(i)>0: print(i, ' Встречалось')
#     else: print(i, ' не встречалось')
#     chislo_2.append(i)


#Матрицы. Исключения
# Матрица - прямоугольная таблица из элементов одного типа.
# A = [[1,4,5], #квадратная матрица
#      [3,4,6],
#      [6,7,9]] #список из списков - это матрица.
# print(A)

#Создание матрицы:

Row = 3 #задали количество строк матрицы
Column = 2 #задали количество столбцов матрицы

# A = [] #в этом пустом списке будет находиться матрица
# for i in range(Row):
#     A.append([0]*Column) #создали матрицу из нулевых элементов с помощью цикла

# A = [[0]*Column for i in range(Row)] #создали матрицу из нулей с помощью генератора
# for i in range(Row):
#     for j in range(Column):
#         A[i][j] = 2
# print(A)

# A = [[1,4,5],
#      [3,4,6],
#      [6,7,9]]
# print('A = ',A)
# print('вторая строка: ', A[1])
# print('третий элемент второй строки: ', A[1][2])

# column = []
# for row in A:
#     column.append(row[2])
# print(column) #вывели на печать 3 столбик матрицы

#Вывод матрицы в прямоугольном виде
# A = [[1,4,5],
#      [3,4,6],
#      [6,7,9]]
# for Row in range(len(A)): #Проходим по номерам строк
#     for Column in range(len(A[Row])): #прошли по номерам столбцов (или по всем элементам строки)
#         print(A[Row][Column], end=' ') #вывод матрицы в прямоугольном виде
#     print()

#Task_1
# Создать матрицу M x N, где M и N вводятся с клавиатуры.
# Элементы матрицы заполнить случайными числами.
# Сделать читабельный вывод матрицы.

# from random import randint
#
# M = int(input('Введите количество строк: '))
# N = int(input('Введите количество столбцов: '))
#
# Matrix = [[0]*M for i in range(N)]
# print(Matrix)
#
# for i in range(M):
#     for j in range(N):
#         Matrix[i][j] = randint(-100,100)
# print(Matrix)
#
# for i in range(len(Matrix)):
#     for j in range(len(Matrix[i])):
#         print(Matrix[i][j], end=' ')
#     print()





#Task_2
# Матрица N x M, можно задать статически.
# Элементы заполняются случайными числами.
# Вводить с клавиатуры число и если оно есть в матрице,
# то вывести индекс строки и колонки в которой оно находится.

# from random import randint
#
# Matrix = [[0]*10 for i in range(10)]
# for i in range(10):
#     for j in range(10):
#         Matrix[i][j] = randint(-100,100)
# for i in range(len(Matrix)):
#     for j in range(len(Matrix[i])):
#         print(Matrix[i][j], end=' ')
#     print()
#
# my_number = int(input('Введите искомое число: '))
# for i in range(len(Matrix)):
#     for j in range(len(Matrix[i])):
#         if my_number == Matrix[i][j]: print(my_number, ' находится на ', i+1, ' строке и на ', j+1, ' столбце')

#Исключения (exceptions)

# a = 100/0 #пример исключения

#Виды исключений:
#1. Базовые исключения (BaseException) - исключение, от которого берут начало все остальные исключения
    #2. SystemExit - системное исключение, происходит из-за функции sys.exit при выходе из программы
    #3. KeyboardInterrupt - прерывание программы (например с помощью Ctrl+F2)
    #while True: k = input() - пример такого исключения
    #4. Exception  - все остальные исключения
        #5. StopIteration - исключение в случае, если в итераторе закончились элементы
        #6. ArithmeticError - арифметическая ошибка
            #ZeroDivisionError - ошибка деления на ноль (a = 100/0)
            #OverflowError - слишком большой результат операции
            #FloatingPointError - ошибка плавающей запятой

#Для обработки исключений используется конструкция try-except
# try: #в этом блоке содержится код, который может вызвать ошибку
#     k = 1/0
# except ZeroDivisionError: #что делать в случае перехвата исключения ZeroDivisionError
#     k = 0
# print(k)

# for i in range(-5,5):
#     try: print(1/i)
#     except ZeroDivisionError: print(i)

# for i in range(-5,5):
#     print(i)
#     try: print(i ** 0.5)
#     except ArithmeticError: print(i) #перехват не только ZeroDivisionError, но и всех остальных арифметических ошибок


# a = {'a':1, 'b':2, 'c':3}
# try: value = a['d']
# except KeyError: print('Такого ключа нет!')

# a = {'a':1, 'b':2, 'c':3}
# try: value = a['d']
# except: print('Такого ключа нет!') #except без названия ошибки будет перехватывать все ошибки

# my_list = [1,2,3,4,5]
# try: my_list[6]
# except IndexError: print('Такого индекса нет')

# a = {'a':1, 'b':2, 'c':3}
# try: value = a['d']
# except IndexError: print('Такого индекса нет!')
# except KeyError: print('Такого ключа нет!')
# except: print('Другая ошибка!')

# a = {'a':1, 'b':2, 'c':3}
# try: value = a['d']
# except (IndexError,KeyError): print('Ошибка!')

# a = {'a':1, 'b':2, 'c':3}
# try:
#     value = a['d']
# except KeyError:
#     print('Такого ключа нет!')
# finally:
#     print('оператор finally отработал успешно!') #оператор finally выполнит блок инструкций даже в том случае,
#     # если была ошибка

# a = {'a':1, 'b':2, 'c':3}
# try:
#     value = a['d']
# except KeyError:
#     print('Такого ключа нет!')
# else: #else работает, если не были перехвачены исключения
#     print('Ошибок нет!')

#Task_3
#Вводятся два числа. Одно число делим на второе. Обработать деление на 0.
# Если ошибок нет, то результат возвести в квадрат. Использовать finally

try:
    a, b = int(input('1 число')), int(input('2 число'))
    c = a/b
except ZeroDivisionError: print('Деление на ноль!')
except ValueError: print('Введите только число!')
else: print(c**2)
finally: print('Готово!')