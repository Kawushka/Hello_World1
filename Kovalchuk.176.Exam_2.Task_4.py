#4.	Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений
# данной буквы в строку. Заглавные буквы нужно считать строчными. Пробелы не учитывать.
stroka = ' An apple a day keeps the doctor away'
b = "".join(stroka.lower().split())
slovar = {i: b.count(i) for i in b}
print(slovar)