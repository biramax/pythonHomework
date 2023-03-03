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

minDif = math.inf # или можно указать разницу с первым элементом списка: abs(X - lst[0])
value = lst[0]

for i in lst:
    dif = abs(X - i)
    if dif < minDif:
        minDif = dif
        value = i

print(f'Значение ближайшего по величине элемента: {value}')


# Другое решение

from random import randint

n = int(input('n = '))
lst = [randint(1, 10) for _ in range(n)]
print(lst)

x = int(input('x = '))

dct = {abs(x - item): item for item in lst}
print(dct)
print(dct[min(dct)])

# или вместо последних трёх строк можно написать

print(min(lst, key=lambda i: abs(i - x)))

"""
lambda i: abs(i - x) - это ананимная функция вместо реальной:

def func(i):
    return abs(i - x)
"""

