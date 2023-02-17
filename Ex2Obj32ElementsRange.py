# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Импорт функций

import os

os.system('cls')

from random import randint

# Заполнение списка

arr = [randint(1, 10) for i in range(int(input('Enter length: ')))]
# Вывод списка
print(*arr)
# Ввод данных
range_min = int(input('Enter numbers range min: '))
range_max = int(input('Enter numbers range max: '))
# Основная функция поиска индексов входящих в диапазон чисел
new_array = []
for i in range(len(arr)):
    if range_min < arr[i] < range_max:
        new_array.append(i)
        # Вывод данных индексами на случай необходимости работы с данными индексами---
        # print(i)
# Вывод данных
print(*new_array)