"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

a = int(input('Первый элемент: '))
b = int(input('Разность: '))
c = int(input('Количество элементов: '))

for i in range(c):
    print(a + i * b, end = ' ')
