# 5.	Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
spis_1 = [1, 12, 6, 7, 8, 4, 100, 25, 28, 39]
spis_2 = [1, 12, 6, 7, 8, 4, 100]
schet = 0
for i in spis_1:
    if i in spis_2: schet += 1
print(schet)