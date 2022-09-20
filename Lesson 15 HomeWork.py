#ДЗ на вторник:
#1. Создать класс Example
#2. Создать в классе 2 статические переменные
#3. Создать в классе 2 динамические переменные
#4. В классе прописать 3 метода
    #4.1 Первый метод: создает любую переменную и выводит ее на печать
    #4.2 Второй метод: возвращает сумму двух переменных, которые определены до класса (то есть глобально)
    #4.3 Третий метод: вывести на печать возведение первой динамической переменной в степень второй динамической переменной
#5. Создать объект этого класса
#6. Вывести на печать все три метода

peremen1 = 200
peremen2 = 500
class Example:
    stat1 = 0
    stat2 = 'fdgfd'
    def __init__(self, dinam1, dinam2):
        self.a = dinam1
        self.b = dinam2
    def print(self, c):
        self.peremennaya = c
        return self.peremennaya
    def summa(self, peremen1, peremen2):
        return peremen1 + peremen2
    def stepen(self):
        return self.a ** self.b
object = Example(2, 6)
print(object.print('fdfgdfdf d sdf s'))
print(object.summa(peremen1, peremen2))
print(object.stepen())