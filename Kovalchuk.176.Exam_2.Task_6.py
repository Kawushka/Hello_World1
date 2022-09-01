# 6.	В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу
import os
os.chdir('D:/')
with open('journal.txt', 'r', encoding="utf8") as f:
    journal = f.read()
    journal = journal.split('\n')
journal_2 = []
for i in journal:
    i = i.split(" ")
    journal_2.append([i[0], i[1], int(i[2])])
count = 0
print('Ученики, чьи оценки ниже 3-х баллов: ')
for i in journal_2:
    count += i[2]
    if i[2] < 3: print(f'{i[0]} {i[1]}')
print(format('Средний балл группы: ' '%.3f' % (count/len(journal_2))))



