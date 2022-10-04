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

# #ВАРИАНТ С ID в первой таблице

# import sqlite3
# conn = sqlite3.connect('Task_2.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS words
# (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')
# conn.commit()
# cursor.execute('''CREATE TABLE IF NOT EXISTS nums
# (numbers INTEGER)''')
# conn.commit()
# my_list = ['Home', 'Work', 29, 9, 2022]
# for i in my_list:
#     if type(i) == str:
#         cursor.execute('''INSERT INTO words(text) VALUES (?)''', (i,))
#         conn.commit()
#         cursor.execute('''INSERT INTO nums(numbers) VALUES (?)''', (len(i),))
#         conn.commit()
#     else:
#         if i %2 ==0:
#             cursor.execute('''INSERT INTO nums(numbers) VALUES (?)''', (i,))
#             conn.commit()
#         else:
#             cursor.execute('''INSERT INTO words(text) VALUES ('нечётное')''')
#             conn.commit()
# cursor.execute('''SELECT * FROM words''')
# count = 0
# # Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# # Создаём список, в который помещаем индексы первой таблицы words
# spis = []
# for i in cursor:
#     spis.append(i[0])
#
# #Считаем, сколько элементов во 2-м списке nums
# cursor.execute('''SELECT * FROM nums''')
# count = 0
# for i in cursor:
#     count += 1
#
# if count > 5:
#     cursor.execute('''DELETE FROM words WHERE id=(?)''', (spis[0],)) #удаляем запись с первым по таблице индексом
#     conn.commit()
#     spis.pop(0) #удаляем из списка 1-ый индекс
# else:
#     cursor.execute('''REPLACE INTO words(id, text) VALUES (1, 'hello')''')
#     conn.commit()
#
# cursor.execute('''SELECT * FROM words''')
# print(*cursor)
# cursor.execute('''SELECT * FROM nums''')
# print(*cursor)

# #ВАРИАНТ БЕЗ ID в первой таблице:

import sqlite3
conn = sqlite3.connect('Task_2.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS words
(text TEXT)''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS nums
(numbers INTEGER)''')
conn.commit()
my_list = ['Home', 'Work', 29, 9, 2022]
for i in my_list:
    if type(i) == str:
        cursor.execute('''INSERT INTO words(text) VALUES (?)''', (i,))
        conn.commit()
        cursor.execute('''INSERT INTO nums(numbers) VALUES (?)''', (len(i),))
        conn.commit()
    else:
        if i %2 ==0:
            cursor.execute('''INSERT INTO nums(numbers) VALUES (?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO words(text) VALUES ('нечётное')''')
            conn.commit()
cursor.execute('''SELECT * FROM words''')
count = 0
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Создаём список, в который помещаем элементы первой таблицы words
spis = []
for i in cursor:
    spis.append(i[0])
print(spis)

#Считаем, сколько элементов во 2-м списке nums
cursor.execute('''SELECT * FROM nums''')
count = 0
if count > 5:
    cursor.execute('''DELETE FROM words WHERE text=(?)''', (spis[0],)) #удаляем запись с первым по таблице элементом
    conn.commit()
    spis.pop(0) #удаляем из списка 1-ый элемент
else:
    cursor.execute('''UPDATE words SET text=('hello') WHERE text=(?)''', (spis[0],))
    conn.commit()

cursor.execute('''SELECT * FROM words''')
print(*cursor)
cursor.execute('''SELECT * FROM nums''')
print(*cursor)