# 1. Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное,
# то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)

import sqlite3, random
conn = sqlite3.connect('Task_1.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table
(id INTEGER PRIMARY KEY AUTOINCREMENT, K_1 INTEGER, K_2 INTEGER)''')
a = random.randint(0,10)
b = random.randint(0,10)
cursor.execute('''INSERT INTO my_table(K_1, K_2) VALUES (?,?)''',(a,b))
conn.commit()

#---ЧАСТЬ КОДА, отвечающая за рандомный индекс
id = cursor.execute('''SELECT id FROM my_table''')
spis = []
for i in id:
    spis.append(i[0])
r = random.choice(spis) #находимый рандомный индекс для выполнения условия "Выберите случайную запись из БД"
print(f'{r} - это случайный индекс из my_table')
#---

cursor.execute('''SELECT ID, K_1, K_2 FROM my_table''')
print('Наша таблица: ', *cursor)
for i in cursor.execute('''SELECT K_1, K_2 FROM my_table WHERE id = (?)''', (r,)):
    if i[0] %2 ==0 and i[1]%2 ==0: #Проверяем, все ли числа этой строки чётные
        print(f'Число {i[0]} и {i[1]} - чётные, удаляем строку с id "{r}"')
        cursor.execute('''DELETE FROM my_table WHERE id = (?)''', (r,))
        conn.commit()
    elif i[0] %2 !=0 and i[1]%2 !=0: #Проверяем, все ли числа этой строки нечётные
        print(f'Число {i[0]} и {i[1]} - нечётные, заменяем значения строку с id "{r}" на (2, 2)')
        cursor.execute('''REPLACE INTO my_table(id, K_1, K_2) VALUES (?,2,2)''',(r,))
        conn.commit()
    else: print('Пока ни одно условие не прошло!')