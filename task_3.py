print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225


def reverse_Number(number): 
	number_reverse = 0
	number_cycle = int(number)
	for digit in range(len(number)):
		if number_cycle % 10 == 0 and digit == len(number) - 1:
			continue
		number_reverse += number_cycle % 10 * 10 ** (len(number) - digit - 1)
		number_cycle //= 10
	number_reverse = str(number_reverse)
	return number_reverse


user_number_one = input('Введите первое число: ')
user_number_two = input('Введите второе число: ')

reverse_number_one = reverse_Number(user_number_one)
reverse_number_two = reverse_Number(user_number_two)
print('\nПервое число наоборот:', reverse_number_one)
print('Первое число наоборот:', reverse_number_two)

summ_reverse_numbers = str(int(reverse_number_one) + int(reverse_number_two))
reverse_summ = reverse_Number(summ_reverse_numbers)
print('\nСумма перевёрнутых чисел:', summ_reverse_numbers)
print('Сумма наоборот:', reverse_summ)