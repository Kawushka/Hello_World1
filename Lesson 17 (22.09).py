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

# Калькулятор с помощью класса
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

# Task 2
# Создать класс, в нем 2 метода
# 1 метод: принимает либо строку, либо число.
# Если строка: если произведение количества гласных и согласных <= длине строки, то вывести все гласные. Иначе все согласные
# Если число: вывести произведение суммы всех четных цифр на длину числа
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


# Методы класса (3 вида)
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

# Уровни доступа атрибутов (Инкапсуляция)
# 1. Private - приватные атрибуты, они недоступны вне класса self.__color = 'Red'
# 2. Public - наоборот доступны везде. По умолчанию все атрибуты публичные self.color = 'Red'
# 3. Protected - тоже самое, что Private, но можно обращаться с атрибутам еще и через классы-потомки self._color = 'Red'

# Класс Human
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

# class Phone:
#     def __init__(self,  start_charge=0):
#        self.__how_many_charges = start_charge
#     def charge(self, value_charge):
#         self.__how_many_charges += value_charge
#         if self.__how_many_charges > 100: self.__how_many_charges = 100
#         print(f'Теперь уровень заряда телефона: {self.__how_many_charges}%')
# MyPhone = Phone(15)
# MyPhone.charge(50)
# MyPhone.charge(50)

# НАСЛЕДОВАНИ В Python
# class <название дочернего класса>(<имя родителя>)
# def __init__(self):
# super().__init__() #вызов инициализатора родителя
# self.a = 10 #добавляем новый функционал
# Создали дочерний класс на основе родительского. В инициализации с помощью команды super().__init__() мы наследуем
# от родительского класса все его методы и свойства.
# Ниже в команде self.a = 10 в дочерний класс мы добавили собственный атрибут

# class Phone:
#     def __init__(self):
#        self.is_on = False
#        self.battery = 0
#     def turn_on(self):
#         self.is_on = True
#
#     def call(self):
#         if self.is_on == True: print('Calling...')
#
# class MyPhone(Phone):
#     def __init__(self):
#         super().__init__() #забрали все свойства и методы родителя
#
#     def charge(self, number_value):
#         self.battery += number_value
#         print(self.battery)
#
# Iphone = MyPhone()
# Iphone.charge(20)
# Iphone.call()
# Iphone.turn_on()
# Iphone.call()

# class Auto:
#     def ride(self):
#         print('Это метод родительского класса')
# class Toyota(Auto):
#     def toyota_method(self):
#         print('Это дочерний метод Тойота')
# class BMW(Auto):
#     def BMW_method(self):
#         print('Это дочерний метод БМВ')
# car_T = Toyota()
# car_T.toyota_method()
# car_B = BMW()
# car_B.BMW_method()

# class Camera:
#     def camera_method(self):
#         print('Метод класса камера')
# class Radio:
#     def radio_method(self):
#         print('Метод класса радио')
# class Phone(Camera, Radio):
#     def Phone_method(self):
#         print('Это дочерний метод класса Phone')
# phone_1 = Phone()
# phone_1.camera_method()
# phone_1.radio_method()


# Task_1.
# 1. Создать класс House
# 1.1. ПРописать динамические свойства _area, _price. Начальные значения получают от входных параметров инита.
# 1.2. Создать метод final_price, который принимает параметр - скидку и показывает стоимость дома с учетом скидки

# 2. Создать класс SmallHouse на основе класса House
# 2.1. В инициализации создать объект площадь 40кв.м.

# 3. В классе Human добавить метод buy_house() для покупки дома
# 3.1 Прописать метод check_money(), который проверяет, что денег достаточно.
# class House:
#     def __init__(self, area, price):
#         self._area = area
#         self._price = price
#     def final_price(self, discount):
#         self._price *= ((100-discount)/100)
#         print('Итоговая стоимость: ', self._price)
#         return self._price
#
# class SmallHouse(House):
#     default_area = 40
#     def __init__(self,stoimost):
#         super().__init__(SmallHouse.default_area, stoimost)
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
# # 3. В классе Human добавить метод buy_house() для покупки дома
# # 3.1 Прописать метод check_money(), который проверяет, что денег достаточно.
#     def check_money(self, dom, skidka):
#         deneg = dom.final_price(skidka)
#         if self.__money >= deneg:
#             self.__by_house(deneg)
#         else:
#             print('Не хватает денег!')
#
#     def __by_house(self, price): #приватный метод
#         print('Куплен дом!')
#         self.__money -= price
#         self.__house = 'Дом есть!'
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
# # # Тесты
# # # Вызовите справочный метод default_info() для класса Human()
# Human.default_info()
# # # Создайте объект класса Human
# Marina = Human('Marina', 32)
# # # Выведите справочную информацию о созданном объекте (вызовите метод info()).
# Marina.info()
# # # Поправьте финансовое положение объекта - вызовите метод earn_money()
# Marina.earn_money(10000)
# Marina.earn_money(50000)
# # # Посмотрите, как изменилось состояние объекта класса Human
# Marina.info()
# marinin_dom = SmallHouse(100000) #создали дом, но пока его не купили
# Marina.check_money(marinin_dom,5)
# Marina.earn_money(20000)
# Marina.check_money(marinin_dom,20)
# Marina.info()

# ПОЛИМОРФИЗМ - один из принципов ООП. Можно использовать одноименные методы в родительском классе и в классе потомке
# class Phone:
#     def __init__(self):
#        self.is_on = False
#        self.battery = 0
#     def turn_on(self):
#         self.is_on = True
#
#     def call(self):
#         if self.is_on == True: print('Calling...')
#     def info(self):
#         print(f'Название класса: {Phone.__name__}')
#
# class MyPhone(Phone):
#     def __init__(self):
#         super().__init__() #забрали все свойства и методы родителя
#
#     def info(self):
#         print(f'Название класса: {MyPhone.__name__}')
#         print(f'Включен ли теелфон: {self.is_on}')
#         print(f'Уровень батареи: {self.battery}')
#
# for i in [Phone,MyPhone]:
#     object = i()
#     object.info() #неявно обращаемся к методу info(). Только в момент исполнения кода станет ясно,
#     #для какого именно объекта этот метод. Это и есть принцип полиморфизма

# Перегрузка метода
# class Car:
#     def start(self, a, b=None):
#         if b is not None:
#             print(a+b)
#         else: print(a)
# car = Car()
# car.start(10,20)

# Инкапсуляция
# class Car:
#
#     def __init__(self, model): #создаем конструктор класса Car
#         self.model = model #инициализация свойства
#
#     @property #создаем свойство модели
#     def model(self):
#         return self.__model
#
#     @model.setter #сеттер для создания свойств
#     def model(self, model):
#         if model<2000:
#             self.__model = 2000
#         elif model >2018:
#             self.__model = 2018
#         else: self.__model=model
#
#     def getModel(self):
#         return 'Год выпуска: ' + str(self.model)
#
# carA = Car(2040)
# print(carA.getModel())

# Task_2
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En')
# и строка, состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе
# он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.
# import string
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#     def print(self):
#         print(self.letters)
#     def letters_num(self):
#         print(len(self.letters))
# class EngAlphabet(Alphabet):
#     __letters = string.ascii_lowercase
#     __letters_num = len(__letters)
#     def __init__(self, lang):
#         super().__init__(lang,EngAlphabet.__letters)
#     def is_en_letter(self, a):
#         if a.lower() in self.__letters and a!='':
#             print('Да')
#         else: print('Нет')
#     def letters_num(self):
#         return self.__letters_num
#
#     @staticmethod
#     def example():
#         print('Hello World!')
#
# test = EngAlphabet('En')
# test.print()
# print(test.letters_num())
# test.is_en_letter('ж')
# test.is_en_letter('J')
# test.example()
# EngAlphabet.example()


# ДЗ на вторник:
# Класс Company:
# 1. Создайте класс Company
# 2.Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста: 1:junior, 2:middle, 3:senior, 4:lead.
# 3.Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром и
# 2) _levels - принимает из словаря levels значение с ключом _index
# 4.Создайте метод _level_up(), который будет переводить программиста на следующий уровень
# 5. Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
# Класс Programmer:
# 1. Создайте класс Programmer
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается параметром, является публичным и
# 2) _level – уровень квалификации на основе словаря из Company
# 3. Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более квалифицированным с помощью метода _level_up()
# 4. Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию.

# Тесты:
# 1.Вызовите справку по программированию
# 2.Создайте объекты классов Company, Programmer
# 3.Используя объект класса Programmer, повысьте свой уровень квалификации
# 4.Дойдите до уровня lead

class Company:
    levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}

    def __init__(self, index):
        if index > 4: index = 4
        self._index = index
        self._levels = self.levels[self._index]

    def _level_up(self):
        if self._index != 4:
            self._index += 1
            self._levels = self.levels[self._index]
            print('Уровень повышен, теперь Вы:', self._levels)

    def is_lead(self):
        if self._index == 4:
            print('Достигнут максимальный уровень!')
        else:
            print('Есть куда расти, Ваш уровень', self.levels[self._index])
        return self._index == 4


class Programmer(Company):

    def __init__(self, name, lev):
        super().__init__(lev)
        self.name = name
        self._level = self.levels[self._index]

    def work(self):
        self._level_up()

    @staticmethod
    def knowledge_base():
        print('Уровень квалификации:')

comp = Company(1)
Kawa = Programmer('Kawa', 1)
Kawa.knowledge_base()
while Kawa.is_lead() == False:
    Kawa.work()