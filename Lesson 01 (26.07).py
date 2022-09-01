# a = 'Hello, world' #красная точка - это точка останова
# for i in a:
#     print(i, end='')

# a = 12
# for i in str(a): #проходим по числу 12 как по строке
#     print(i)

# a =12
# for i in range(a): #range - это диапазон всех чисел от 0 до 12 не включительно
#     print(i)

# a =12
# for i in range(a):
#     if i%2 == 0:  #% остаток от деления, if i%2 == 0 условие на то, что переменная i делится на 2 без остатка
#         print(i)

# a = 'Hello, world' #красная точка - это точка останова
# for i in a:
#     if i == 'd': #условие будет выполняться если == дает значение True
#         print(i, end='')

# a = 'Hello, world' #красная точка - это точка останова
# for i in a:
#     if True: #if True всегда будет верным
#         print(i, end='')

# a =12
# for i in range(a):
#     if i%2 != 0:  #if i%2 != 0 условие на то, что переменная i не делится на 2 без остатка
#         print(i)

# a = 12
# a = str(a) #меняем тип переменной на строковую str, для того чтобы проходить по этому числу посимвольно
# print(type(a))

# a = 'Hello World'
# b = 12
# b = str(12)
# for i in b:
#     print(i)
#
# print(b)
# b = 10
# c = 1 + b #переменная с взяла последнее значение b
# print(c)

# for i in range(3): #параметр i проходит по числам от 0 до 3
#     print(i)

# for i in range(3,8): #первый аргумент - это начало диапазона, второй аргумент конец диапазона
#     print(i)

# for i in range(3,8,1): #третий аргумент это шаг диапазона
#     print(i)

# for k in range(1,10):
#     if k == 3:
#         break #break - досрочный выход из цикла
#     print(k)

# for k in range(1,10):
#     if k == 5:
#         continue #continue минует оставшееся тело цикла и продолжает цикл со следующего шага
#     print(k)

# a = [1,2,3,4,'f','8','8*t,.'] #в квадратные заключаются элементы списка (list)
# for i in a:
#     if type(i) is str: #сделали проверку на то, что элемент является строкой
#         print(i)

# for i in range(1,10):
#     print(i)
# i = i+1
# print(i)

# while 1==1: #условие цикла
#     print('Hello') #тело цикла

# a = 10
# while a<20:#цикл выполняется, пока а не увеличится до 20
#     print(a)
#     a = a+1 #в цикле while обязательно изменяем параметр а. Иначе цикл будет бесконечным

#Отличие for/while - for это цикл по диапазону, while это цикл по условию

# for i in range(3): #цикл for выполняется до тех пор, пока итератор не обойдет весь диапазон значений
#     print('Привет')

# a = True
# while a: #Простейшее условие, которое всегда будет выполняться, за исключением если мы не изменим его на False
#     print('Hello')
#     a = False


# a = 10
# while a: #Любое число кроме 0 в условии воспринимается как True, 0 как False
#     print('Hello')
#     a = 0

# i = 10
# while i>0:
#     print(i)
#     i -= 1 #переменная i уменьшается на 1 (i = i-1)
# else:
#     print('Done!') #конструкция else в цикле while срабатывает если цикл доходит до конца

# i = 10
# while i>0:
#     print(i)
#     i -= 1 #переменная i уменьшается на 1 (i = i-1)
#     if i ==4:
#         break
# else:
#     print('Done!') #конструкция else в цикле while не срабатывает если цикл не доходит до конца из-за break или ошибки

# i = 10
# for k in str(i):
#     if k == '1':
#         break
#     print(k)
# else:
#     print('Готово!') #else работает в цикле for аналогично как в while

# while True:
#     a = float(input('Введите первое число: '))
#     znak = input('Введите операцию (+,-,*,/): ')
#     if znak in '+-*/':
#         b = float(input('Введите второе число: '))
#         if znak == '+':print(a+b)
#         elif znak == '-':print(a-b)
#         elif znak == '*':print(a*b)
#         elif znak == '/':
#             if b == 0:print('Нельзя делить на ноль!')
#             else:print(a/b)
#     else:
#         print('Некорректная операция!')
#         break

import random #импортируем модуль для работы со случайными числами
# a = random.randint(1,100) #создаем случайное целое значение от 1 до 100
# print(a)
# a = random.random() #создаем случайное значение от 0 до 1
# print(a)
# a = random.choice(['Sveta','Marina','Artem','Dima','Irina','Artem']) #случайный выбор из вашего списка
# print(a)

#ДЗ: игра камень-ножницы-бумага с использованием цикла while и random.choice. while i<3 or j<3. if i>j: print('Вы победили!')

import random
i=0
j=0
while i<3 and j<3:
    print('Счёт: ', i, ':', j)
    a = random.choice(['Камень', 'Ножницы', 'Бумага'])
    b = random.choice(['Камень', 'Ножницы', 'Бумага'])
    print('1: ', a)
    print('2: ', b)
    if a == b:
        continue
    elif a == 'Камень' and b == 'Ножницы':
        i += 1
    elif a == 'Камень' and b == 'Бумага':
        j += 1
    elif a == 'Ножницы' and b == 'Камень':
        j += 1
    elif a == 'Ножницы' and b == 'Бумага':
        i += 1
    elif a == 'Бумага' and b == 'Камень':
        i += 1
    else:
        j += 1
print('Счёт: ', i, ':', j)
if i > j: print('Победил игрок 1')
else: print('Победил игрок 2')
