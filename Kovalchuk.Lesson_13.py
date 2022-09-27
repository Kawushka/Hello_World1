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