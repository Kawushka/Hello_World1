# 1. Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит пустая строка
# a = input('Введите строку: ')
# with open('new_file.txt', 'w') as f:
#     while a != '':
#         f.write(a + '\n')
#         a = input('Введите строку: ')
# with open('new_file.txt', 'r') as f: print(*f)

# 2. Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.
# a = [1,2,7,3, 'ffggg','8','qp']
# a_str = []
# a_int = []
# for i in a:
#     if type(i) is int: a_int.append(i)
#     elif type(i) is str:
#         if i.isdigit(): a_int.append(int(i))
#         else: a_str.append(i)
# a_str.sort(key=len)
# a_int.sort()
# with open('new_file.txt','w') as f:
#     for i in a_str: f.write(i + '\n')
#     for i in a_int: f.write(f'{str(i)}  \n')

# 3. C помощью модуля os добавьте на свой рабочий стол папку my_folder,
# в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.

# import os
# os.chdir('C:/Users/37533/OneDrive/Рабочий стол') #меняем директорию на рабочий стол
# os.mkdir('my_folder') #на рабочем столе создали папку my_folder
# os.chdir('my_folder')
#
# with open('test_1.txt', 'w') as f:    f.write('text1') #автоматически будет создан файл test_1
# with open('test_2.txt', 'w') as f:    f.write('text2')
# with open('test_3.txt', 'w') as f:    f.write('text3')

# os.rename('test_1.txt', 'rename_1.txt')
# os.rename('test_2.txt', 'rename_2.txt')
# os.rename('test_3.txt', 'rename_3.txt')

# os.remove('rename_1.txt')
# os.remove('rename_2.txt')
# os.remove('rename_3.txt')
# os.chdir('..')
# os.rmdir('my_folder')

# f1 = ['a','b','c']
# f2 = ['b','a','c']
# print(f1==f2)

# a = ['gg','ll','kk']
# a.remove('ll')
# a.pop(1)
# del a[1]
# a[1:2] = []
# print(a)

# cort = ('ttt','hhhh','jjj') #заменить hhhh на llll
# cort = list(cort)
# cort[1] = 'llll'
# cort = tuple(cort)
# print(cort)

#(12)
# cort = (12,)
# cort = tuple('feff')
# print(cort)

# print(tuple([12]))

# cort = ('ttt',['hhhh',12],'jjj')
# cort[1][1] = 10
# print(cort)

# cort_1 = ('ttt','hhhh','jjj')
# cort_2 = ('ttt','hhhkkh','jjjkkk')
# print(min(cort_1))

# dict_1 = {'a':12, (1,2,3,4):'g'}
# dict_1['a'] = 15
# # del dict_1['a']
# print(dict_1.get('a'))
# print(dict_1)
#
# list_first = [
#                 1,2,3,
#                 {
#                     'a':1,
#                     'b':2,
#                     'c':{'abc':20,
#                          'def':30,
#                          'ghi':40}
#                 }
# ]
# #Выведем на печать начение 40
# print(list_first[3]['c']['ghi'])

# my_slovar = {'green':1, 'blue':2,'yellow':3}
# for i in my_slovar:
#     print(i, my_slovar[i])

# my_slovar = {'green':1, 'blue':2,'yellow':3}
# print(
#     my_slovar.keys()
# )

# print(type({}))
# s = set()
# print(type(s))

# a = [1,2,3,4,5,5,5,7,7]
# # print(len(a))
# a = set(a)
# # print(len(a))
#
# a.remove(1)
# a.discard(8)
# try: a.remove(8)
# except KeyError: pass
# print(a)

# a = {1,2,3,4,5,5,5,7,7}
# a.add(8)

# HGFTiour - сколько пар заглавных и сколько пар строчных
# a = 'HGFTiour'
# count1, count2 = 0,0
# for i in range(1,len(a)):
#     if a[i-1].isupper() and a[i].isupper(): count1 += 1
#     elif a[i - 1].islower() and a[i].islower(): count2 += 1
# print(count1, count2)

# with open('new_file.txt', encoding='utf-8') as f: print(*f)