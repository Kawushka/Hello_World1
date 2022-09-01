# s = ['f','h','j','y',66,43,10,677,10,11] #каждый третий с конца
# print(s[::-3])
# print(s[-1:0:-3]) #печатает от конца до первого элемента, так как 0 не включается

# Task_1. С клавиатуры вводится 7-значное число.
# Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1, 3 и 6 цифры.
# input_number = input('Введите семизначное число: ')
# while len(input_number) != 7: input_number = input('Введите семизначное число: ')
# chet =0
# nechet = 0
# summa = 0
# for i in input_number:
#     if int(i)%2 == 0: chet += 1
#     else: nechet += 1
#     summa += int(i)
# if chet>nechet: print(f'Сумма всех цифр: {summa}')
# else: print(f'Произведение 1,3 и 6 цифр числа: {int(input_number[0])*int(input_number[2])*int(input_number[5])}')

#Task_2.С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.
# # В случае равенства вывести на экран все гласные буквы. Латинскую букву y считать как согласную.
# input_text = input('Введите любой текст: ')
# glas = 0
# sogl = 0
# gl = ''
# for i in input_text:
#     if i.lower() in 'aeouiёуеыаоэяию':
#         glas +=1
#         gl += i
#     elif i.isalpha(): sogl += 1 #проверка на то, что i является буквой
# print(f'Количество гласных: {glas}, количество согласных: {sogl}')
# if glas==sogl: print(gl)

#Task_3.
# Посчитать, сколько раз встречается определенная цифра в числах.
# Количество введенных чисел и искомая цифра задаются с клавиатуры. Сами числа выбираются рандомно.
import random
# input_count = int(input('Введите количество чисел: '))
# input_find = input('Введите искомую цифру: ')
# rand_number = [random.randint(0,1000) for i in range(input_count)]
# count_find = 0
# print(str(rand_number))
# for i in str(rand_number): объявляем список строкой
#     if i == input_find: count_find +=1
# print(count_find)

# for i in rand_number: через двойной цикл
#     for j in str(i):
#         if j == input_find: count_find +=1
# print(f'Цифра {input_find} встретилась {count_find} раз')

# Task_4. Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке отдельно вывести на экран.
# Строка может содержать пробелы.

# input_str = input('Введите строку: ')
# dig = ''
# for i in input_str:
#     if i.isdigit(): dig += i
# print(dig)

#Task_5. Пользователь вводит строку. Посчитать, сколько в ней пар строчных и сколько пар заглавных букв.
# PPKoHoGGjj - 3 пары заглавных, 1 пары строчных
# input_str = input('Введите строку: ')
# upper_str = 0
# lower_str = 0
# # print(len(input_str)) - выведет 10
# for i in range(1, len(input_str)):
#     # isupper() islower() - методы для проверки, что буква заглавная или строчная
#     if input_str[i-1].isupper() and input_str[i].isupper():
#         upper_str += 1
#     elif input_str[i-1].islower() and input_str[i].islower():
#         lower_str += 1
# print(f'В строке {input_str} заглавных пар: {upper_str}, строчных пар: {lower_str}')

#Кортежи (tuple)
# list1 = [1,2,3,4] #список
# tuple1 = (1,2,3,4) #кортеж
# print(list1,tuple1)
# print(type(list1), type(tuple1))
# a = (1,) #для объявления кортежа с одним элементом используется запятая
# print(type(a))
# a = tuple([1])
# print(type(a))
# a = tuple() - пустой кортеж
# print(a)

# a = [1,2,3,4,5,6]
# b = (1,2,3,4,5,6)
#
# print(a.__sizeof__())#размер списка в байтах
# print(b.__sizeof__()) #размер кортежа в байтах
#Преимущества кортежа: защита от изменений и меньший размер

# b = (1,2,3,4,5,6) #из кортежа можно извлекать элементы по индексу
# print(b[0:3])
# print(b[1])
# b[1] = 2 #выдаст ошибку, так как элементы изменять нельзя
# b = (1,2,3,4,5,6)
# c = list(b)
# c[1] = 10
# b = tuple(c)
# print(b) #изменили кортеж b путем изменения типа данных на list

# b = (1,2,3,4,5,6,['yy','uuu'])
# # b[6] = 'ppp' - нельзя изменить элемент кортежа
# b[6][1] = 'ppp'#можно изменить элементы списка, который лежит в кортеже
# print(b)
#
# a1 = (1,2,3,4)
# b1 = (5,6,7,8)
# c1 = a1+b1 #можно объединять кортежи
# print(c1)
#
# d1 = a1*2
# print(d1)

#Функции pop, insert, extend, remove, append использовать нельзя, так как кортеж неизменяемый
#Можно использовать count, len
# f = (1,3,5,7,9)
# print(f.count(5), len(f)) #количество 5, длина кортежа
# print(max(f), min(f)) #максимальный и минимальный элементы
# f = ('bgifljdflkdfj','agg')
# print(max(f), min(f)) #максимальная и минимальная строка по алфавиту
# print(max(f,key=len), min(f,key=len)) #по длине строки

#Task_1. Создать кортеж из 10 случайных чисел. Найти минимальное и максимальное число
# import random
# a = tuple(random.randint(1,1000) for i in range(10))
# print(a)
# print(max(a), min(a))

# Task_2. Заполнить кортеж 10 случайными числами от 0 до 5. ВТорой кортеж от -5 до 0.
# Объединить два кортежа в третий. Вывести на экран третий кортеж и количество 0 в нем.

# import random
# a = tuple(random.randint(0,5) for i in range(10))
# b = tuple(random.randint(-5,0) for i in range(10))
# c = a+b
# print(c, c.count(0))

# c = list(input('Введите числа: '))
# for i in range(len(c)):
#     c[i] = int(c[i])
# c = tuple(c)
# print(c)

#Task_3. Вывести все элементы кортежа без скобок
# c = ('one','two','three')
# print(c[0],c[1],c[2])
# print(*c) # символ * отображает все элементы внутри переменной c
# print(' '.join(c))

#Task_4. Создать два кортежа из чисел.
# 1. Найти, в каком кортеже сумма элементов больше
# 2. По каждому кортежу вывести порядковые номера минимальных элементов

# c = (1, 56, 5.6, 7.9999999, 13)
# d = (43, 9.000001, 65, 1000, 0.00002)
# sum_1 = sum(c)
# sum_2 = sum(d)
# # print(format(sum_1, '.2f'))
# # print('%.3f' % sum_1)
# if sum_1>sum_2: print('Сумма больше в первом кортеже')
# elif sum_2>sum_1: print('Сумма больше во втором кортеже')
# else: print('Сумма одинаковая в обоих кортежах')
# print(c.index(min(c))+1)
# print(d.index(min(d))+1)
