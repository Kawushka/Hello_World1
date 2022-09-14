a = (13244, 43, 'gff')
b = ['gfgffg', '3443', '434ggf', 145]
c = 578
d = 'Anna, go HOme'
e = {1:'nnn', 2:'vvv'}
f = True
def f(x):
    if type(x) == tuple:
        print(f'Длина кортежа {x}:', len(a))
    elif type(x) == list:
        stroka = 0
        chislo = 0
        for i in x:
            if type(i) == int: chislo += 1
            else: stroka +=1
        print(f'Кол-во строк в {x}: {stroka}, кол-во чисел: {chislo}')
    elif type(x) == int:
        chet = 0
        nechet = 0
        for i in str(x):
            if int(i) %2 == 0: chet += 1
            else: nechet += 1
        print(f'Кол-во чётных цифр в числе {x}: {chet}, нечётных: {nechet}')
    elif type(x) == str:
        glasn = 0
        soglasn = 0
        for i in x:
            if i.lower() in 'aeiou': glasn += 1
            elif i.isalpha() == True: soglasn += 1
        print(f'В строке "{x}" кол-во гласных букв: {glasn}, согласных: {soglasn}')
    else: print('ОК')
f(a)
f(b)
f(c)
f(d)
f(e)
f(f)