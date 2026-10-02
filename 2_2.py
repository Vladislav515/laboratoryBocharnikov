price = int(input('Цена тетради в рублях: '))
count = int(input('Количество тетрадей: '))
paid = int(input('Переданная сумма: '))
cost = price * count
change = paid - cost
print(f'Стоимость: {cost}, сдача: {change}')