print('Задача 4. Урок информатики 3')

# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась, 
# ведь на следующем уроке нужно будет объяснить такие страшные слова, 
# как «экспоненциальное», «мантисса» и «порядок».
 
# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно. 
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу, 
# которая выводит отдельно мантиссу и отдельно порядок этого числа.


def mantiss_and_scale(number):
	count = 0
	if number <= 1:
		while number < 1:
			number *= 10
			count -= 1
		number = round(number, 15)
	else:
		output_number = number
		while number > 10:
			number /= 10
			count += 1
		number = round(output_number * 10 ** (-count ), count)
	return number, count


user_number = input('Введите число: ')
user_number = float(user_number.replace(',', '.'))
mantiss, scale = mantiss_and_scale(user_number)
print('Мантисса: ', mantiss, ', порядок: ', scale, end = '')		
