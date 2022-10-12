# ДЗ на вторник:
# Дописать кнопки и их функции, а также дописать их в метод ravno
# 1. Умножение
# 2. // (с делением на ноль) +
# 3. % как остаток от деления (деление на ноль) +
# 4. Степень +
# 5. Возведение в квадрат (не спрашивать второй операнд)
# 6. Сделать верстку всех кнопок для их компактного размещения на окне

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__() #наследуем функционал класса QWidget
        self.initUI() #метод для создания GUI
        self.operand_1 = '' #хранится первое число
        self.operand_2 = '' #хранится второе число
        self.my_input = '' #здесь хранится то, что мы выводим на экран калькулятора


    def initUI(self):
        self.setGeometry(300, 300, 220, 400) #координаты углов окна приложение, X,Y, ширина, высота
        self.setWindowTitle('Калькулятор') #название приложения
        self.label = QLabel(self) #создаём лейбл
        self.label.setText('0') #начальное значение в лейбле
        self.label.resize(220, 100) #размер Label
        my_font = QFont("Times New Roman", 14)
        self.label.setFont(my_font) #установил шрифт окна label Times New Roman и 12 размер
        self.label.setAlignment(Qt.AlignCenter) #текст label по центру
        self.label.setStyleSheet("""
            font: bold;
            color: white;
            background-color: black;
        """)
        # self.move(0, 0) #переместили окно в верхний угол

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(55, 50)
        self.num_7.move(0, 200)
        self.num_7.clicked.connect(self.seven)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(55, 50)
        self.num_8.move(55, 200)
        self.num_8.clicked.connect(self.eight)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(55, 50)
        self.num_9.move(110, 200)
        self.num_9.clicked.connect(self.nine)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(55, 50)
        self.num_4.move(0, 250)
        self.num_4.clicked.connect(self.four)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(55, 50)
        self.num_5.move(55, 250)
        self.num_5.clicked.connect(self.five)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(55, 50)
        self.num_6.move(110, 250)
        self.num_6.clicked.connect(self.six)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(55, 50)
        self.num_1.move(0, 300)
        self.num_1.clicked.connect(self.one)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(55, 50)
        self.num_2.move(55, 300)
        self.num_2.clicked.connect(self.two)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(55, 50)
        self.num_3.move(110, 300)
        self.num_3.clicked.connect(self.three)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(55, 50)
        self.num_0.move(55, 350)
        self.num_0.clicked.connect(self.zero)

        self.num_point = QPushButton('.', self)
        self.num_point.resize(55, 50)
        self.num_point.move(110, 350)
        self.num_point.clicked.connect(self.point_f)

        self.plus = QPushButton('+', self)
        self.plus.resize(55, 50)
        self.plus.move(165, 300)

        self.plus.clicked.connect(self.plus_f)

        self.minus = QPushButton('-', self)
        self.minus.resize(55, 50)
        self.minus.move(165, 250)
        self.minus.clicked.connect(self.minus_f)

        self.mul = QPushButton('*', self)
        self.mul.resize(55, 50)
        self.mul.move(165, 200)
        self.mul.clicked.connect(self.mul_f)

        self.div = QPushButton('/', self)
        self.div.resize(55, 50)
        self.div.move(165, 150)
        self.div.clicked.connect(self.div_f)

        self.div_remainder = QPushButton('/%', self)
        self.div_remainder.resize(55, 50)
        self.div_remainder.move(110, 150)
        self.div_remainder.clicked.connect(self.div_remainder_f)

        self.integer_division = QPushButton('//', self)
        self.integer_division.resize(55, 50)
        self.integer_division.move(55, 150)
        self.integer_division.clicked.connect(self.integer_division_f)

        self.exponentiation = QPushButton('x^y', self)
        self.exponentiation.resize(55, 50)
        self.exponentiation.move(0, 150)
        self.exponentiation.clicked.connect(self.exponentiation_f)

        self.exponentiation_2 = QPushButton('x^2', self)
        self.exponentiation_2.resize(55, 50)
        self.exponentiation_2.move(0, 100)
        self.exponentiation_2.clicked.connect(self.exponentiation_2_f)

        self.ravno = QPushButton('=', self)
        self.ravno.resize(55, 50)
        self.ravno.move(165, 350)
        self.ravno.setFont(QFont("Times New Roman", 12))
        self.ravno.clicked.connect(self.ravno_f)

        self.clear = QPushButton('C', self)
        self.clear.resize(55, 50)
        self.clear.move(110, 100)
        self.ravno.setFont(QFont("Times New Roman", 12))
        self.clear.clicked.connect(self.clear_f)

# Ф У Н К Ц И И:
    def enterValue(self):
        if self.label.text() == '0' or self.m == 1:
            self.label.setText('')
            self.m=0
        self.label.setText(self.label.text() + self.my_input)
    def one(self):
        self.my_input = '1'
        self.enterValue()
    def two(self):
        self.my_input = '2'
        self.enterValue()
    def three(self):
        self.my_input = '3'
        self.enterValue()
    def four(self):
        self.my_input = '4'
        self.enterValue()
    def five(self):
        self.my_input = '5'
        self.enterValue()
    def six(self):
        self.my_input = '6'
        self.enterValue()
    def seven(self):
        self.my_input = '7'
        self.enterValue()
    def eight(self):
        self.my_input = '8'
        self.enterValue()
    def nine(self):
        self.my_input = '9'
        self.enterValue()
    def zero(self):
        self.my_input = '0'
        self.enterValue()
    def plus_f(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('0')
    def minus_f(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('0')
    def mul_f(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('0')
    def div_f(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('0')
    def div_remainder_f(self): #остаток от деления
        self.operation = '/%'
        self.operand_1 = float(self.label.text())
        self.label.setText('0')
    def integer_division_f(self): #целочисленное деление
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('0')
    def exponentiation_f(self): #возведение в степень
        self.operation = 'x^y'
        self.operand_1 = float(self.label.text())
        self.label.setText('0')
    def exponentiation_2_f(self): #возведение в квадрат
        self.m = 1
        self.operation = 'x^2'
        self.operand_1 = float(self.label.text())
        self.label.setText(str(self.operand_1 ** 2))
    def clear_f(self):
        self.label.setText('')
    def point_f(self):
        if '.' not in self.label.text():
            self.my_input = '.'
            self.enterValue()
    def ravno_f(self):
        self.m = 1
        self.operand_2 = float(self.label.text())
        if self.operation == '+':                                 #ПЛЮС
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '-':                               #МИНУС
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '*':                               #УМНОЖИТЬ
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '/%':                              #ОСТАТОК ОТ ДЕЛЕНИЯ
            if self.operand_2 == 0:
                self.rezult = 'Деление на НОЛЬ!'
            else: self.rezult = int(self.operand_1 % self.operand_2)
        elif self.operation == '/':                               #ДЕЛЕНИЕ
            if self.operand_2 == 0:
                self.rezult = 'Деление на НОЛЬ!'
            else: self.rezult = self.operand_1 / self.operand_2
        elif self.operation == '//':                              #ЦЕЛОЕ ОТ ДЕЛЕНИЯ
            if self.operand_2 == 0:
                self.rezult = 'Деление на НОЛЬ!'
            else:
                self.rezult = int(self.operand_1 / self.operand_2)
        elif self.operation == 'x^y':                              #ВОЗВЕДЕНИЕ В СТЕПЕНЬ
            self.rezult = self.operand_1 ** self.operand_2
        elif self.operation == 'x^2':                              #В КВАДРАТЕ
            self.rezult = self.operand_1 ** 2

        self.label.setText(str(self.rezult))



app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec())

#ВОПРОСЫ:
# 3. Как сделать так, чтобы после ввода первого числа и после нажатия на функцию, оставалось введённое число в label,
# а далее при вводе второго операнда label обнулялся... Как эту логику поменять в коде, ведь у нас после нажатия функции
# (умножения, деления и т.д.) обнуляется label и в поле появляется "0"

