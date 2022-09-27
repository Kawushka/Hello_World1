# 4. Создайте класс на тему животных. Используйте статические и динамические переменные, дочерний (1 или более)
# классов на конкретное животное. Публичные и приватные методы. Полиморфизм (одинаковые названия методов info в обоих
# классах, которые выводят информацию о животных, либо о конкретном животном данного класса).
# Создайте объекты каждого класса и обратитесь к каждому методу.
# Напишите один staticmethod, один classmethod, к которым также обратитесь.

class Animals:
    count = 0

    def __init__(self, name):
        self.name = name
        Animals.count += 1

    def eat(self):                                       # Есть
        print(f'{self.name} поел')

    def sleep(self):                                    # Спать
        print(f'{self.name} спит')

    def info(self):
        print(f'Создано {Animals.count} животных')

    @staticmethod
    def info_animals():
        print('Класс животные')


class Cats(Animals):
    count = 0
    def __init__(self, name):
        self.name = name
        super().__init__(self.name)
        Cats.count += 1

    def purr(self):                                 # Помурчать
        print(f'{self.name} замурчал')

    @staticmethod
    def info_cats():
        print(f'Создано кошек: {Cats.count}')

    @classmethod
    def classmethod(cls):
        print('Кошки милые')

class Dogs(Animals):
    count = 0

    def __init__(self, name):
        self.name = name
        super().__init__(self.name)
        Dogs.count += 1

    def growl(self):                                # Рычать
        print('Рррррр, страшно?')

    def bark(self):                                 # Гавкать
        print(f'{self.name} чё-то загавкал')

    @staticmethod
    def info_dogs():
        print(f'Создано собак: {Dogs.count}')


dog1 = Dogs('Шарик')
dog2 = Dogs('Рэкс')
dog3 = Dogs('Мухтар')
cat1 = Cats('Том')
cat2 = Cats('Лили')
cat3 = Cats('Ева')
cat1.eat()
cat1.purr()
cat1.sleep()
dog2.sleep()
dog2.bark()
dog1.eat()
dog1.info()
Cats.info_cats()
Animals.info_animals()
Cats.classmethod()