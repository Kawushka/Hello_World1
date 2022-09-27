# # #ДЗ на вторник:
# # #1. Создать класс Example
# # #2. Создать в классе 2 статические переменные
# # #3. Создать в классе 2 динамические переменные
# # #4. В классе прописать 3 метода
# #     #4.1 Первый метод: создает любую переменную и выводит ее на печать
# #     #4.2 Второй метод: возвращает сумму двух переменных, которые определены до класса (то есть глобально)
# #     #4.3 Третий метод: вывести на печать возведение первой динамической переменной в степень второй динамической переменной
# # #5. Создать объект этого класса
# # #6. Вывести на печать все три метода
# #
#
#
# per_1 = 20
# per_2 = 3
# class Example:
#     example_1 = 'физика'
#     rating = 7
#     def __init__(self, example_one, rating_one):
#         self.myexample = example_one
#         self.myrating = rating_one
#     def a(self):
#         per = 5
#         print(per)
#
#     def b(self):
#         return per_1+per_2
#
#     def c(self):
#         print(f'возведение {self.myexample**self.myrating}')
# fizika = Example(10,2)
# fizika.a()
# print(fizika.b())
# fizika.c()

#Калькулятор с помощью класса
# class Calculator:
#
#     def __init__(self): #метод инициализации вызывается сразу при обращении к объекту класса
#         self.vvod()
#
#     def vvod(self):
#         self.a = int(input('Введите первое число: '))
#         self.b = int(input('Введите второе число: '))
#
#     def summ(self):
#         return self.a + self.b
#     def raz(self):
#         return self.a - self.b
#     def mul(self):
#         return self.a * self.b
#     def div(self):
#         if self.b == 0:
#             return 'error'
#         else:
#             return self.a / self.b
#
# while True:
#     x = input('Введите операцию: ')
#     if x == '': break
#     if x not in '+-*=': continue
#     example = Calculator()
#
#     if x == '+':
#         print(example.summ())
#     if x == '-':
#         print(example.raz())
#     if x == '*':
#         print(example.mul())
#     if x == '/':
#         print(example.div())

#Task 2
#Создать класс, в нем 2 метода
# 1 метод: принимает либо строку, либо число.
    #Если строка: если произведение количества гласных и согласных <= длине строки, то вывести все гласные. Иначе все согласные
    #Если число: вывести произведение суммы всех четных цифр на длину числа
# 2 метод: возвращает длину числа или строки.

# class proverka:
#
#     def first(self, a):
#         if type(a) == str:
#             glasn = 0
#             soglasn = 0
#             gl_sp = []
#             sog_sp = []
#             for i in a:
#                 if i.lower() in 'aouei':
#                     glasn +=1
#                     gl_sp.append(i)
#                 elif i.isalpha():
#                     soglasn += 1
#                     sog_sp.append(i)
#             if glasn*soglasn <= self.dlina(a): print(gl_sp)
#             else: print(sog_sp)
#         elif type(a) == int:
#             summ_chet = 0
#             for i in str(a):
#                 if int(i)%2 == 0: summ_chet += int(i)
#             print(summ_chet*self.dlina(a))
#     def dlina(self,a):
#         return len(str(a))
# test = proverka()
# test.first('tteeeee')
# test.first(444)

# class Car:
#     def __str__(self):
#         return 'Car class object'
#     def start(self):
#         print('Двигатель заведен')
# tesla = Car()
# print(tesla)


#Методы класса (3 вида)
    # 1. Метод экземпляра класса (обычный метод) - такие методы доступны после объявления экземпляра класса
    # 2. Статические методы @staticmethod - обычные функции, которые ограничены областью видимости класса
# class Phone:
#     @staticmethod
#     def model_phone(model):
#         if model == 'A':
#             return 123
#         else:
#             return None
# print(Phone.model_phone('A'))
    # 3. Метод класса @classmethod
# class Phone:
#     def __init__(self,color, model, os):
#         self.os = os
#         self.model = model
#         self.color = color
#     @classmethod
#     def toy_phone(cls, color):
#         toyphone = cls(color, 'ToyPhone', None)
#         return (toyphone.color, toyphone.os, toyphone.model)
# print(Phone.toy_phone('Blue'))

#Уровни доступа атрибутов (Инкапсуляция)
    # 1. Private - приватные атрибуты, они недоступны вне класса self.__color = 'Red'
    # 2. Public - наоборот доступны везде. По умолчанию все атрибуты публичные self.color = 'Red'
    # 3. Protected - тоже самое, что Private, но можно обращаться с атрибутам еще и через классы-потомки self._color = 'Red'

#Класс Human
# 1. Создайте класс Human.
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
#       Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
#       В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# 5. Реализуйте справочный статический метод default_info(),
#       который будет выводить статические поля default_name и default_age.
# 6. Реализуйте метод earn_money(), увеличивающий значение свойства money.



# class Human:
#     default_name = 'John'
#     default_age = 40
#
#     def __init__(self,name=default_name,age=default_age):
#         #Публичные атрибуты
#         self.name = name
#         self.age = age
#         #Приватные атрибуты
#         self.__money = 0
#         self.__house = None
#
#     def info(self):
#         print(self.name, self.age, self.__money, self.__house)
#
#     @staticmethod
#     def default_info():
#         print(Human.default_name, Human.default_age)
#
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Получили {amount}. Теперь у нас {self.__money} денег')
#
# # Тесты
# # Вызовите справочный метод default_info() для класса Human()
# Human.default_info()
# # Создайте объект класса Human
# Marina = Human('Marina', 32)
# # Выведите справочную информацию о созданном объекте (вызовите метод info()).
# Marina.info()
# # Поправьте финансовое положение объекта - вызовите метод earn_money()
# Marina.earn_money(10000)
# Marina.earn_money(50000)
# # Посмотрите, как изменилось состояние объекта класса Human
# Marina.info()


# ДЗ на четверг:
# В классе Phone завести приватное свойство __how_many_charges, которое покажет уровень заряда телефона.
# Для изменения заряда телефона прописать метод charge(), в котором меняется значение приватного свойства.

class Phone:

    def __init__(self):
        self.__how_many_charges = 0

    def charge(self, amount):
        self.__how_many_charges += amount
        print(self.__how_many_charges)

a = Phone()
a.charge(20)


