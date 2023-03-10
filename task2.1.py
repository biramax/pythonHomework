"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

while True:
    numCoins = int(input('Введите число монет: '))
    if numCoins < 0 or numCoins % 1 != 0:
        print('Введённые данные некорректны.')
    else:
        break

numToRevert = 0
numSide = 0 # Число орлов

for i in range(numCoins): # 0 1 2 3 4
    side = int(input(f'Монета #{i + 1} (орёл - 0, решка - 1): '))
    if side:
        numSide += 1

print(f'Минимальное количество монет, которые нужно перевернуть: {numSide if numSide <= numCoins // 2 else numCoins - numSide}')

# Второй способ

from random import randint

coins = [randint(0, 1) for _ in range(int(input()))]
print(coins)
print(min(coins.count(0), coins.count(1)))