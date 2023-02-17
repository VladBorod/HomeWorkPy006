# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# Импорт функции

import os

os.system('cls')

# Ввод данных

first_elm = int(input('Enter first elm: '))
difference = int(input('Enter difference: '))
amount = int(input('Enter amount: '))

# Поиск последнего элемента

last_element = first_elm + ((amount - 1) * difference)

# Создание массива
array = []
# Сохдание временной переменной
temp = first_elm
# Помещение первого числа в массив
array.append(first_elm)
# Создание цикла уменьшенного на 1 элемент, т.к. первый элемент уже в нем
for i in range(amount-1):
    temp += difference
    array.append(temp)

# Вывод данных

print('Last element: ', last_element)
print(array)
