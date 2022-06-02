# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
# 
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
# 
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
# 
# Известно, что глубина точно больше нуля и меньше четырёх метров.
# 
# Обеспечьте контроль ввода.
# 
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
# 
# Приблизительная глубина безопасной кладки: 0.732421875 м


def  digit_count(number):
	count = 0
	while number < 1:
		count += 1
		number *= 10
	return count

def qubical_equation_trigonometrically(number):
	import math
	#print('Имеем уравнение вида x ** 3 + a * x ** 2 + b * x + c = 0')
	a = -3
	b = -12
	c = 10  - number
	Q = (a ** 2 - 3 * b) / 9
	R = (2 * a ** 3 - 9 * a * b + 27 * c) / 54
	S = Q ** 3 - R ** 2
	#print('\nQ =', Q, '\nR =', R, '\nS =', S)
	if S > 0:
		#print('Уравнение имеет три вещественных корня')
		fi = math.acos(R / (Q ** (3/2))) / 3
		x1 = -2 * Q ** (1/2) * math.cos(fi) - a / 3
		x2 = -2 * Q ** (1/2) * math.cos(fi + 2 * math.pi / 3) - a / 3
		x3 = -2 * Q ** (1/2) * math.cos(fi - 2 * math.pi / 3) - a / 3
		#print('\nfi =', fi, '\nпервый корень:', x1, '\nвторой корень:', x2, '\nтретий корень:', x3)
	elif S == 0:
		#print('Уравнение имеет меньше трёх различных корней')
		x1 = 2 * R ** (1 / 3) - a / 3
		x2 = R ** (1 / 3) - a / 3
	else:
		#print('Уравнение имеет один вещественный корень')
		fi = math.acosh(abs(R) / (abs(Q) ** (3/2))) / 3
		x1 = -2 * abs(Q) ** (1/2) * math.cosh(fi) - a / 3
		#print('\nfi =', fi, '\nпервый корень:', x1)
		
	if x1 > 0 and x1 < 4:
		target = x1
	if x2 > 0 and x2 < 4:
		target = x2
	if x3 > 0 and x3 < 4:
		target = x3
	return target
		
		
acceptable_level = input('Введите допустимый уровень риска: ')
acceptable_level = float(acceptable_level.replace(',' , '.'))

round_level = digit_count(acceptable_level)
depth = qubical_equation_trigonometrically(acceptable_level)
print('Глубина отбора пробы:', round(depth, round_level), 'метров')
