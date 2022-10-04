# 3. Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд и записать их в текстовый файл (название и время).

import sqlite3
conn = sqlite3.connect('Task_3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS music
(songs TEXT, time INTEGER)''')
a = input('Введите песню: ')
b = int(input('Введите длительность в секундах: '))
cursor.execute('''INSERT INTO music(songs, time) VALUES (?,?)''',(a,b))
conn.commit()

cursor.execute('''SELECT * FROM music''')
file = open('Task_3.txt', 'a')
for i in cursor:
    if i[1]>60: file.write(str(i) + '\n')
