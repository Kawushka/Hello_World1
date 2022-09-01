# 2. Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.

massiv = [[70, 3, 'slovo1', 'dlinnoeslovo'], [1, 150, 89, 'slovechko2'], ['dlinnoeslovechko', 1, 15, 90]]
chisla = []
slova = []
for i in massiv:
    for j in i:
        # print(j)
        if type(j) == int: chisla.append(j)
        else: slova.append(j)
slova.sort(key=len)
chisla.sort()
f = open('Kovalchuk.Lesson_8.Task_2.txt', 'a')
for i in slova:
    f.write(f'{i} ')
for i in chisla:
    f.write(f'{str(i)} ')
f.close()