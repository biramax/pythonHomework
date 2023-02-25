"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

while True:
    N = int(input('Введите натуральное число: '))
    if N < 0 or N % 1 != 0:
        print('Введённые данные некорректны.')
    else:
        break

"""
power  = 1
powN   = 2
output = ''
while powN <= N:
    output += str(powN)+' '
    powN = pow(2, power := power + 1)    

print(output)
"""

# Второе решение

var = 2
while var := var * 2 <= N:
    print(var)
