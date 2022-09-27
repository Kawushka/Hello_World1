class Animals:
    count = 0
    def __init__(self, name):
        self.name = name
        Animals.count += 1

    def info(self):
        print(f'Имя: {self.name}.')
        print(f'Кол-во животных: {self.count}')

    def what_the_animal(self):
        type_of_the_animal = 0
        if self.name == "Лось":
            print('Это млекопитающее')
            type_of_the_animal = 1
        elif self.name == 'Сова':
            print('Это птица')
            type_of_the_animal = 2
        elif self.name == 'Комар':
            print('Это насекомое')
            type_of_the_animal = 3
        elif self.name == 'Карась':
            print('Это рыба')
            type_of_the_animal = 4
        else:
            print('Класс животного не определён')
            type_of_the_animal = 0
        return type_of_the_animal

class Mode(Animals):

    def __init__(self):
        super().__init__(self.name)

    def run(self):
        if self.what_the_animal() == 1:
            print('Побежали')
        elif self.what_the_animal() == 2:
            print('Полетели')
        elif self.what_the_animal() == 3:
            print('Полетели')
        elif self.what_the_animal() == 4:
            print('Поплыли')
        else: print('Не знаем, что делать')
        return self.what_the_animal()


# anim_1 = Animals('Лось')
# anim_2 = Animals('Сова')
# anim_3 = Animals('Комар')
# anim_4 = Animals('Карась')
# anim_5 = Animals('Утка')
print(f'Создано животных: {Animals.count}')
# anim_1.what_the_animal()
# anim_5.what_the_animal()
rrr = Mode()
rrr.run()
