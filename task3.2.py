"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""

import random, math

while True:
    N = int(input('Введите длину списка: '))
    if N < 0 or N % 1 != 0:
        print('Введённые данные некорректны.')
    else:
        break

while True:
    X = int(input('Введите натуральное число: '))
    if X < 0 or X % 1 != 0:
        print('Введённые данные некорректны.')
    else:
        break

lst = [random.randint(1, 10) for _ in range(N)]

print(f'Массив: {lst}')

minDif = math.inf
value = 0

for i in lst:
    dif = abs(X - i)
    if dif < minDif:
        minDif = dif
        value = i

print(f'Значение ближайшего по величине элемента: {value}')