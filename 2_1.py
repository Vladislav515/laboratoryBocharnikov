total_seconds = int(input('Введите число секунд: '))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f'{hours} ч. {minutes} мин. {seconds} сек.')