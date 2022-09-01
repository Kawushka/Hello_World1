# У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

tovar = {'Apple': [4.5, 10], 'Orange': [6.2, 5], 'Pineapple': [10.0, 1], 'Mango': [7.5, 2], 'Banana': [3.8, 10]}
# print(tovar['Orange'])
a = ''
price = 0
for key in tovar:
    print(f'{key} - {tovar[key][0]} - {tovar[key][1]}')
while a != 'n':
    a = input('What? (n - nothing) ')
    if a == 'n':
        print(f'Price: {price}')
        for key in tovar:
            print(f'{key} - {tovar[key][0]} - {tovar[key][1]}')
        break
    if a in tovar:
        b = int(input('How many? '))
        if b <= tovar[a][1]:
            tovar[a] = tovar[a][0], (tovar[a][1] - b)
            price += tovar[a][0] * b
        else: print(f'Maximum amount {tovar[a][1]}')
    else: print('Product not found!')
