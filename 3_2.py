num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == '+':
    result = num1 + num2
    print(f"{result:.2f}")
elif op == '-':
    result = num1 - num2
    print(f"{result:.2f}")
elif op == '*':
    result = num1 * num2
    print(f"{result:.2f}")
elif op == '/':
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = num1 / num2
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")