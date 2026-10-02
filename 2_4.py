total = int(input('Количество сообщений: '))
capacity = int(input('Сообщений на странице: '))
full_pages = total // capacity
remain = total % capacity
pages_needed = (total + capacity - 1) // capacity
print(f'Полных страниц: {full_pages}, остаток: {remain}, всего: {pages_needed}')