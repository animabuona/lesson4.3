def number_tens_form(number):
	issue = number
	count = 0
	if number >= 1:
		while issue > 10:
			issue /= 10
			count += 1
	elif number <= 0:
		print('Это число не подходит')
	else:
		while number < 1:
			count -= 1
			number *= 10
	print(number, '=', issue, '* 10 **', count)


user_number = input('Введите число: ')
user_number = float(user_number.replace(',', '.'))
number_tens_form(user_number)
