# ДЗ на четверг:
# Ivanov.Lesson_8.Task_1.py Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка
# Ivanov.Lesson_8.Task_2.py Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.
# Ivanov.Lesson_8.Task_3.py C помощью модуля os добавьте на свой рабочий стол папку my_folder,
# в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.

# 1. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка

# f = open('Kovalchuk.Lesson_8.Task_1.txt', 'a')
# vvod = []
# while vvod != '':
#     vvod = input('Введите текст (для окончания записи оставьте строку пустой): ')
#     f.write(vvod)
#     f.write('\n')
# f.close()
# print('Информация сохранена!')

# 2. Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.

# massiv = [[70, 3, 'slovo1', 'dlinnoeslovo'], [1, 150, 89, 'slovechko2'], ['dlinnoeslovechko', 1, 15, 90]]
# chisla = []
# slova = []
# for i in massiv:
#     for j in i:
#         # print(j)
#         if type(j) == int: chisla.append(j)
#         else: slova.append(j)
# slova.sort(key=len)
# chisla.sort()
# f = open('Kovalchuk.Lesson_8.Task_2.txt', 'a')
# for i in slova:
#     f.write(f'{i} ')
# for i in chisla:
#     f.write(f'{str(i)} ')
# f.close()

# 3 C помощью модуля os добавьте на свой рабочий стол папку my_folder,
# в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.

# import os
# os.mkdir('C:/Users/Kawa/Desktop/my_folder')
# os.chdir('C:/Users/Kawa/Desktop/my_folder')
# f1 = open('test_1.txt', 'w')
# f1.close()
# f2 = open('test_2.txt', 'w')
# f2.close()
# f3 = open('test_3.txt', 'w')
# f3.close()
# os.rename('test_1.txt', 'rename_1.txt')
# os.rename('test_2.txt', 'rename_2.txt')
# os.rename('test_3.txt', 'rename_3.txt')
# os.remove('rename_1.txt')
# os.remove('rename_2.txt')
# os.remove('rename_3.txt')
# os.chdir('C:/Users/Kawa/Desktop')
# os.rmdir('my_folder')
