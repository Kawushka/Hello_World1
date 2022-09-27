# Task_1.
# 1. Создать класс House
# 1.1. ПРописать динамические свойства _area, _price. Начальные значения получают от входных параметров инита.
# 1.2. Создать метод final_price, который принимает параметр - скидку и показывает стоимость дома с учетом скидки
#
# 2. Создать класс SmallHouse на основе класса House
# 2.1. В инициализации создать объект площадь 40кв.м.
#
# 3. В классе Human добавить метод buy_house() для покупки дома
# 3.1 Прописать метод check_money(), который проверяет, что денег достаточно.
class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    def final_price(self, discount):
        self._price *= ((100-discount)/100)
        print('Итоговая стоимость: ', self._price)
        return self._price

class SmallHouse(House):
    default_area = 40
    def __init__(self,stoimost):
        super().__init__(SmallHouse.default_area, stoimost)
class Human:
    default_name = 'John'
    default_age = 40

    def __init__(self,name=default_name,age=default_age):
        #Публичные атрибуты
        self.name = name
        self.age = age
        #Приватные атрибуты
        self.__money = 0
        self.__house = None

# 3. В классе Human добавить метод buy_house() для покупки дома
# 3.1 Прописать метод check_money(), который проверяет, что денег достаточно.
    def check_money(self, dom, skidka):
        deneg = dom.final_price(skidka)
        if self.__money >= deneg:
            self.__by_house(deneg)
        else:
            print('Не хватает денег!')

    def __by_house(self, price): #приватный метод
        print('Куплен дом!')
        self.__money -= price
        self.__house = 'Дом есть!'

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, amount):
        self.__money += amount
        print(f'Получили {amount}. Теперь у нас {self.__money} денег')

# # Тесты
# # Вызовите справочный метод default_info() для класса Human()
Human.default_info()
# # Создайте объект класса Human
Marina = Human('Marina', 32)
# # Выведите справочную информацию о созданном объекте (вызовите метод info()).
Marina.info()
# # Поправьте финансовое положение объекта - вызовите метод earn_money()
Marina.earn_money(10000)
Marina.earn_money(50000)
# # Посмотрите, как изменилось состояние объекта класса Human
Marina.info()
marinin_dom = SmallHouse(100000) #создали дом, но пока его не купили
Marina.check_money(marinin_dom,5)
Marina.earn_money(20000)
Marina.check_money(marinin_dom,20)
Marina.info()
