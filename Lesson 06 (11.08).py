# a = tuple(i for i in range(10)) генератор кортежа от 0 до 9
# print(a)

# Task_1 Найти самое длинное слово в строке
# string = 'Я изучаю язык программирования Python'
# words = string.split(' ') #разбили строку по пробелам
# # print(max(words, key=len))
# max_word = 0 #номер максимального слова
# for i in range(len(words)):
#     if len(words[i]) > len(words[max_word]): #длину текущего слова сравниваем с длиной самого длинного слова
#         max_word = i #если условие выполнится, то теперь это слово будет самым длинным
# print(words[max_word])

#Словарь (dict)
# a = ['ghh',456,'hh'] #у каждого элемента списка есть номер (индекс)
# d = {'d1':'ghh', 12:456, 'd3':'hh'} #словарь состоит из пар (ключ:значение)
# print(d)
# print(d[12]) #к значениям словаря можно обращаться по ключу, как в списках по индексу
# print(d['d1'])
# d = {} #создали пустой словарь
# print(type(d))

# d = dict(short='dict', long='dictionary')
# print(d['short'])

# d = dict([(1,'1'),('2',4)])
# print(d)

# d= dict.fromkeys(['a','b'])
# print(d)
# d['a'] = 10
# print(d)
# d = dict.fromkeys(['a','b'],100)
# print(d)

#Создадим словарь d, где каждому ключу соответствует этот же ключ в квадрате
# d = {i:i**2 for i in range(8)} #генератор словаря
# print(d)
# d[5]=1000 #обращаемся к значению словаря по ключу этого значения
# print(d)
# d.clear() #очистка словаря
# print(d)
# c = d.copy() #сделали копию словаря, но в другой ячейке памяти
# print(id(c), id(d))
# print(*d.items()) #items - метод для извлечения всех пар словаря
# d.pop(5) #удаляет пару с заданным ключем
# print(d)
# print(d.pop(5)) #удаляется пара и выводится на печать значение
# print(d)
# print(d.keys()) #все ключи
# print(d.values()) #все значения
# print(len(d)) #количество пар словаря

# Months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul',8:'Aug',9:'Sep',10:'Oct',
#           11:'Nov',12:'Dec', 'S':1000}
# count = len(Months) #в переменную count внесли количество месяцев
# print(count)
# del D[key] - конструкция для удаления элемента словаря по ключу
# del Months[6] - удалили месяц под 6 номером
# del Months[13] #если указать несуществующий ключ, то выдаст ошибку KeyError
# del Months['S'] #удалили элемент с ключем 'S'

# Positions = {'Manager':('Director','Deputy Director'),
#             'Teacher':('Specialict','Methodist','Lecturer'),
#             'Staff':('Cleaner','Watchman')
#              } #словарь со вложенными кортежами. Ключи - это позиции, а значения - это кортежи с подпозициями
# print(len(Positions))
# print(len(Positions['Manager']))
# print(len(Positions['Staff']))
# print(type({'Director','Deputy Director'})) - множество (set)
# f_is = key in D #проверяем, существует ли ключ key в словаре D (True, False)
# f_is = 'Teache' in Positions #пример
# print(f_is)

Salary = {'Director':12000,
          'Secretary':10000,
          'Cleaner':100000}
key = 'Secretary'
# if key in Salary:
#     del Salary[key] #Secretary удалится, если он есть. Иначе не будет ошибки
# print(Salary)
# del Salary['Secretary'] #Если такого ключа нет, то будет ошибка
# print(Salary)
# f_is = key not in D #проверяет, что ключ отсутствует в словаре
# print('Cleaner' not in Salary)

# Words = dict() #создаем пустой словарь
# count = int(input('Введите количество пар: '))
#
# while count>0:
#     wrd = input('Введите ключ: ')
#     value = input('Введите значение: ')
#     if wrd not in Words:
#         Words[wrd] = value
#         count -= 1
# print(Words)

#zip - объединяет список ключей и список значений
# Number = dict(zip([1,2,3],['One','Two','Three'])) # для каждого ключа из первого списка прикрепили значение из второго списка
# print(Number)

# Months = {1:'Jan',
#           2:'Feb',
#           3:'Mar',
#           4:'Apr',
#           5:'May',
#           6:'Jun',
#           7:'Jul',
#           8:'Aug',
#           9:'Sep',
#           10:'Oct',
#           11:'Nov',
#           12:'Dec'
#           }
# for mn in Months:
#     print(f'{mn}: {Months[mn]}') #обход словаря с выводом на печать ключей и их значений

#Сортировка словаря (по ключам)
# A = {'f':10, 'a':2, 'c':12}
# #1.Вытащить все ключи
# ak = A.keys()
# #2. Конвертировать ключи в список
# ak = list(ak)
# #3. Отсортировать этот список ключей
# ak.sort()
# #4. Вывести новый словарь в отсортированном виде
# B = {}
# for k in ak:
#     B[k] = A[k]
# print(B)

#Task_1
#Создать словарь person с ключами name, age, city, sex. Вывести на печать все возраста.

# person1 = {'name':'Artem','age':29, 'city':'Minsk','sex':'M'}
# person2 = {'name':'Dima','age':35, 'city':'Brest','sex':'M'}
# person3 = {'name':'Sveta','age':45, 'city':'Minsk','sex':'W'}
# person4 = {'name':'Marina','age':32, 'city':'Vileika','sex':'W'}
# person5 = {'name':'Irina','age':35, 'city':'Bobruisk','sex':'W'}
# person6 = {'name':'Vladimir','age':39, 'city':'Minsk','sex':'M'}
# person7 = {'name':'Kristina','age':38, 'city':'Minsk','sex':'W'}
# persons = (person1,person2,person3,person4,person5,person6,person7)
# for i in persons:
#     print(i['age'])

#Task_2.
# Создадим словарь с ключами BMW, Tesla. Для каждого ключа сделать список из трех моделей этой марки.
# Вывести первое и последнее значение по каждому ключу.

# auto = {'BMW':['X5', 'X6', 'X7'],'Tesla':['Model_S','Model_X','Model_A']}
# print(auto['BMW'][0], auto['BMW'][-1])
# print(auto['Tesla'][0],auto['Tesla'][-1])

#Task_3
# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(d1["b"] == d2["b"])

#Task_4
# Все числовые значения словаря перемножить и вывести на экран
# my_dictionary = {'ffff':123, 'ggg':789,'hhhh':1000000}
# result = 1
# for key in my_dictionary:
#     result = result * my_dictionary[key]
# print(result)

# Task_5
# a = [1,2,3,4,5]
# b = ['a','b','c','d','e']
# c = dict(zip(a,b))
# print(c)

#Task_6.
# Из строки pythonist ключами сделать буквы этой строки, а значениями количество упоминаний этой буквы в строке.
# my_str = 'pythonist'
# my_dict = {i:my_str.count(i) for i in my_str} #генератор словаря
# print(my_dict)
