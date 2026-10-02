n = int(input("Введите n: "))

count = 0
total = 0

for _ in range(n):
    number = int(input("Введите число: "))
    if number < 0 and number % 2 != 0:
        count += 1
        total += number

print(f"Количество {count}, сумма {total}")