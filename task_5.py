print('Задача 5. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.
        
def  digit_count(number):
	count = 0
	while number > 0:
		count += 1
		number //= 10
	return count

def digit_cross(number):
	last_digit = number % 10
	scale = digit_count(number)
	first_digit = number // (10 ** (scale - 1))
	between_digits = number  % 10 ** (scale - 1) // 10
	criss_cross = last_digit * 10 ** (scale - 1) + between_digits * 10  + first_digit
	return criss_cross

first_user_number = int(input('Введите первое число: '))
count = digit_count(first_user_number)
while count < 3:
	print('Число цифр в числе должно быть не меньше трёх')
	first_user_number = int(input('Введите первое число: '))
	count = digit_count(first_user_number)
first_reverse_number = digit_cross(first_user_number)
print('Первое изменённое число:', first_reverse_number)

second_user_number = int(input('Введите второе число: '))
count = digit_count(second_user_number)
while count < 4:
	print('Число цифр в числе должно быть не меньше четырёх')
	second_user_number = int(input('Введите второе число: '))
	count = digit_count(second_user_number)
second_reverse_number = digit_cross(second_user_number)
print('Второе изменённое число:', second_reverse_number)

summ = first_reverse_number + second_reverse_number
print('Сумма изменённых чисел:', summ)
