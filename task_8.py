print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709


def factorial_of_number(number):
	factoriall = 1
	for member in range(1, number + 1):
		factoriall *= member
	return factoriall	
		
def number_degree(number, degree):
	issue = 1
	for point in range (degree ):
		issue *= number
	return issue


user_number = input('Введите число: ')
user_number = float(user_number.replace(',', '.'))
precision = input('Введите требуемую точность результата: ')
precision = float(precision.replace(',', '.'))

sum_member = 0
result = 0
row_member = 1

while abs(row_member) > precision:
	member_degree = number_degree(-1, sum_member)
	user_number_degree = number_degree(user_number, sum_member * 2)
	member_factorial = factorial_of_number(2 * sum_member)
	row_member = member_degree * user_number_degree / member_factorial
	sum_member += 1
	result += row_member
	
print('Сумма ряда с точностью', precision, 'равна', result)


		
		
		
		



