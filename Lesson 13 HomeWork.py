# ДЗ на вторник:
# Калькулятор с помощью пользовательских функций
# Функции: сложение, вычитание, умножение, деление (обработать исключение деления на ноль)
# Пятая операция тоже через функцию (для выхода из калькулятора)
# По желанию использовать декоратор

c = ['+', '-', '*', '/']
act = " "
while act != "":
    def plus(a, b):
        return float(a) + float(b)


    def minus(a, b):
        return float(a) - float(b)


    def umnoj(a, b):
        return float(a) * float(b)


    def delenie(a, b):
        try:
            return float(a) / float(b)
        except ZeroDivisionError:
            print('Деление на ноль!')


    def exit():
        print('Спасибо за использование калькулятора!')


    vvod1 = input('Введите первое число: ')
    act = input('Укажите действие:\n'
                '"+" - сложение \n'
                '"-" - вычитание\n'
                '"*" - умножение\n'
                '"/" - деление\n'
                'Для выхода ничего не указывайте\n'
                'Ваш выбор: ')
    if act in c:
        vvod2 = input('Введите второе число: ')
        if act == "+":
            print(f'Сумма двух чисел: {vvod1} + {vvod2} = {plus(vvod1, vvod2)}')
        elif act == "-":
            print(f'Разница двух чисел: {vvod1} - {vvod2} = {minus(vvod1, vvod2)}')
        elif act == "*":
            print(f'Произведение двух чисел: {vvod1} * {vvod2} = {umnoj(vvod1, vvod2)}')
        elif act == "/":
            if delenie(vvod1, vvod2) != None: print(f'Частное двух чисел: {vvod1} / {vvod2} = {delenie(vvod1, vvod2)}')
    elif act == "": exit()
    else: print('Неверное действие')
