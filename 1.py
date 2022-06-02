count = 0
number = float(input('Введите число: '))
summand = number
while 1 + number < 2:
  count += 1
  number += summand
print('Количество действий:', count)