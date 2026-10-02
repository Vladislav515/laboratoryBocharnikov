n = int(input("Введите n: "))

first = int(input("Введите число: "))
total = first
positive = 1 if first > 0 else 0
maximum = first

for _ in range(n - 1):
    number = int(input("Введите число: "))
    total += number
    if number > 0:
        positive += 1
    if number > maximum:
        maximum = number

print(f"Сумма {total}, положительных {positive}, максимум {maximum}")