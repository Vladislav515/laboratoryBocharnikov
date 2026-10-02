value = int(input("Введите число от 0 до 100: "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 24:
    print("Начало")
elif value <= 84:
    print("В процессе")
else:
    print("Завершение")