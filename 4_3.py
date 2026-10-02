number = int(input("Введите целое число: "))
rejected = 0

while number <= 0:
    rejected += 1
    number = int(input("Введите целое число: "))

print(f"Квадрат {number * number}, отклонено {rejected}")