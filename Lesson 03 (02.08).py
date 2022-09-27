# a = [1,2,3,4,'gfgfg', 'hhgghgh',90000]
# #вывести первый, средний и последний элементы списка
# print(a[0]) #первый элемент
# print(a[-1]) #последний элемент
# if len(a)%2 == 0: #проверяем на четность количество элементов
#     print(a[len(a)//2],a[len(a)//2 - 1]) #печатали соседние элементы (средние)
# else: print(a[len(a)//2])#один средний элемент

# b = [1,2,3,3,4,2,7,8,9,0] #отсортировать список и оставить только уникальные элементы
# for i in b:
#     if b.count(i)>1: b.remove(i)
# b.sort(reverse=True)
# print(b)

# b = [1,2,3,3,4,2,7,8,9,0]
# b.reverse()
# print(b)

# c = [1,2,3,[5,6],[7,'k']]
# print(c[3][1]) #выводим на печать 6 из вложенного списка
# count = 0
# for i in c:
#     if type(i) is list:
#         for j in i:
#             count +=1
#         count -= 1
#     count += 1
# print(count)

#Заменить первый элемент на [1,2,3]. В конец списка добавить сумму этого вложенного списка
# a = [1,2,3]
# c[0] = a
# c.append(sum(a))
# print(c)
# c[0] = [1,2,3]
# c.append(sum(c[0]))
# print(c)

#c[:] - весь список

#c.count(2) #количество двоек
#отличие remove от del в том, что del берет индекс, а remove берет значение

# x:= 1 #Pascal
# x <- 4
# let x = 100
# x = 4 Python

# x = 2 #int
# x = float(x)
# print(type(x))

# print(id(x))

# spisok_strok = ['dgg','gffggf','srrsc']
# print(','.join(spisok_strok)) #в join сначала указываем, каким символом разделять объединенные строки
# print('gfv,gv fg'.split(',')) #у split в конце пишем символ, по которому нужно разорвать строку
#
spisok_strok = ['dgg','gffggf','srrsc']
sp_2 = ''.join(spisok_strok)
print(sp_2)
# # d g g g ff g g fsrrsc
# sp_2 = (sp_2).split('g',2)
# print(sp_2)

# a = [1,2,3,4,5,6,7,8,9,10] #каждый третий элемент с конца
# print(a[::-3]) #первые два аргумента можно не указывать, так как проход по всему списку

# print('@10sl @fl99 @pfd98p'.count('@')) #считает количество @
# print('@10sl @fl99 @pfd98p'.count('@',0,7)) #считает с 0 по 7 позицию
# print('@10sl @fl99 @pfd98p'.count('@',5)) #считает с 5 позиции

# for i in 'abc':
#  print(1)
#  print(1)
#  print(1)
# print(1)

# print(1 + 2) if '999'.isdigit() else print('No') - команда с постусловием (сначала команда, потом условие)

#while может использовать ==, !=, <,>,<=,>=, is, is not, <>, True, False,0, 1,3,4,5...
# w = True
# while w:
#     print(w)
#     w = False

# for k in range(1,100):
#     k -= 10
# print(k)

# k = 0
# while k<100:
#     k += 1
#     break
# else: print('Цикл работает корректно') #else сработает если цикл завершен корректно (не было break)
# k -= 10
# print(k)
#else в циклах for, while означает "если был break, то завершить цикл, ИНАЧЕ выполнить команду print

# for i in range(100):
#     if i%2 ==0:
#         continue #четные числа пропускаем и не выводим на печать
#     print(i)

#Task_1
#Имеется два списка чисел.
# 1.Найти их пересечение
# 2.уникальные элементы первого списка
# 3.уникальные элементы второго списка.

# from random import randint
# a = [randint(0, i) for i in range(randint(1, 10))] #выводим случайное число от 1 до 10 случайное количество раз
# b = [randint(0, i) for i in range(randint(1, 10))]
# print(a, b)
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)
# d1 = []
# d2 = []
# for i in a:
#     if a.count(i)==1: d1.append(i)
# for i in b:
#     if b.count(i)==1: d2.append(i)
#
# print(d1,d2)
