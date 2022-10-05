#Обновление данных в таблице - редактирование какой-то записи в таблице (UPDATE)

# #ДЗ на вторник:
# 1. Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное,
# то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)

#
# import random
# import sqlite3
#
# conn = sqlite3.connect('Task_1.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS task1
# (id INTEGER PRIMARY KEY AUTOINCREMENT, num1 INTEGER, num2 INTEGER)''')
# x = random.randint(0,10)
# y = random.randint(0,10)
# cursor.execute('''INSERT INTO task1(num1, num2) VALUES (?,?)''',(x,y))
# conn.commit()
# cursor.execute('''SELECT id FROM task1''')
# k = cursor.fetchall() #знаесли в переменную все записи из таблицы
# # k = *cursor #*cursor нельзя занести в переменную, поэтому лучше использовать fetchall()
# r = random.choice(k) #случайная запись из таблицы
# print(r)
# cursor.execute('''SELECT num1,num2 FROM task1 WHERE id=?''',r)
# for i in cursor:
#     print(i)
#     if i[0]%2 ==0 and i[1]%2==0:
#         cursor.execute('''DELETE FROM task1 WHERE id=?''',r)
#
#     elif i[0]%2 !=0 and i[1]%2 !=0:
#         # cursor.execute('''UPDATE task1 SET num1=2, num2=2 WHERE id=?''',r)
#         # #обновили в таблице task1 запись в строке под номером r, в SET указали новые значения
#         cursor.execute('''REPLACE INTO task1 (id, num1, num2) VALUES (?,2,2)''',r)
#         #REAPLCE в таблице task1 значения в id, num1, num2 заменил на ?,2,2
# conn.commit()
# cursor.execute('''SELECT * FROM task1''')
# print(*cursor)

# 2. Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
#  my_list = [‘Home’, ‘Work’, 29, 9, 2022]
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
# если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»
#
# import random
# import sqlite3
# my_list = ['Home', 'Work', 29, 9, 2022, None]
# conn = sqlite3.connect('Task_2.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS task2_1
# (id INTEGER PRIMARY KEY AUTOINCREMENT, num1 TEXT)''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS task2_2
# (id INTEGER PRIMARY KEY AUTOINCREMENT, num2 INTEGER)''')
# for i in my_list:
#     if type(i) == str:
#         cursor.execute('''INSERT INTO task2_1(num1) VALUES (?)''', (i,))
#         conn.commit()
#         cursor.execute('''INSERT INTO task2_2(num2) VALUES (?)''', (len(i),))
#         conn.commit()
#     elif type(i) == int:
#         if i%2: #if i%2 вернет True если число нечетное, то есть остаток равен 1
#             cursor.execute('''INSERT INTO task2_2(num2) VALUES (?)''',(i,))
#             conn.commit()
#         else:
#             cursor.execute('''INSERT INTO task2_1(num1) VALUES ('Нечетное') ''')
#             conn.commit()
# cursor.execute('''SELECT * FROM task2_1''')
# zapisi1 = cursor.fetchall() #fetchall вытаскивает все записи в виде списка
# print(zapisi1)
# cursor.execute('''SELECT * FROM task2_2''')
# zapisi2 = cursor.fetchall() #fetchall вытаскивает все записи в виде списка
# print(zapisi2)
#
# if len(zapisi2)>25:
#     cursor.execute('''DELETE FROM task2_1 WHERE id=?''',(zapisi1[0][0],))
#     conn.commit()
# elif len(zapisi2)<25:
#     cursor.execute('''UPDATE task2_1 SET num1='Hello' WHERE id=?''',(zapisi1[0][0],))
#     conn.commit()
#
# cursor.execute('''SELECT * FROM task2_1''')
# print(*cursor)
# cursor.execute('''SELECT * FROM task2_2''')
# print(*cursor)

# 3. Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд и записать их в текстовый файл (название и время).

# import sqlite3
# conn = sqlite3.connect('Task_3.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS music
# (songs TEXT, time INTEGER)''')
# a = input('Введите песню: ')
# b = int(input('Введите длительность в секундах: '))
# cursor.execute('''INSERT INTO music(songs, time) VALUES (?,?)''',(a,b))
# conn.commit()

# cursor.execute('''SELECT * FROM music''')
# file = open('Task_3.txt', 'a')
# for i in cursor:
#     print(i)
#     if i[1]>60: file.write(str(i) + '\n')
# file.close()

# with open('text.txt','w') as f:
#     for i in cursor:
#         print(i)
#         if i[1]>60: f.write(str(i) + '\n')


#Task_4. Создайте метод класса для работы с БД (Таблица из одной колонки типа INteger)
# В БД:
# Если передан 1 аргумент, вставить в таблицу запись с числом 3
# Если переданы 2 аргумента: проверить является ли второй аргумент числом.
# Если условие верно, то удалить первую запись с БД
# Если переданы 3 аргумента, первые 2 любого типа, а 3 является числом,
# то обновить на число 77 третью запись.

# import sqlite3
# conn = sqlite3.connect('Task_4.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1
# (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
#
# class A:
#     def proverka(self, a=None,b=None,c=None): #=None означает, что у аргумента будет пустое значение, если он не указан
#         if a != None and b == None and c == None: #если указан только первый аргмент
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES(3)''')
#             conn.commit()
#         elif a != None and b != None and c == None:
#             if type(b) == int:
#                 cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
#                 conn.commit()
#         elif a != None and b != None and type(c) is int:
#             cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
#             conn.commit()
#
# a = A() #нет инициализации, поэтому при создании объекта аргументы не указываем
# a.proverka(100)
# cursor.execute('''SELECT id,col_1 FROM tab_1''')
# print(*cursor)
# a.proverka(100,200)
# cursor.execute('''SELECT id,col_1 FROM tab_1''')
# print(*cursor)
# a.proverka(100,200,300)
# cursor.execute('''SELECT id,col_1 FROM tab_1''')
# print(*cursor)
# a.proverka(100,200,'h')
# cursor.execute('''SELECT id,col_1 FROM tab_1''')
# print(*cursor)

#Task_5. Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на: hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки. Первая – id, вторая и третья с данными.

import sqlite3
conn = sqlite3.connect('Task_5.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1
(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
conn.commit()

# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES(3,6)''')
# conn.commit()
cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
conn.commit()
cursor.execute('''UPDATE tab_1 SET col_1='Hello', col_2='World' WHERE id=3''')
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)

#  *Записать данные с таблицы в файл в три колонки. Первая – id, вторая и третья с данными.
with open('new_file.txt','w') as f:
    for i in k:
        f.write(f'{str(i[0])}:\t{str(i[1])}\t{str(i[2])}\n')

# 1: 3  6
# 2: Hello  World