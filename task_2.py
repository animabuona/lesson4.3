def max_of_two_numbers(number_a, number_b):
	max_1_2 = (number_a + number_b + abs(number_b - number_a)) / 2
	return max_1_2
  
def max_of_three_numbers(number_a, number_b, number_c):
	max_1_2 = max_of_two_numbers(number_a, number_b)
	max_1_3 = max_of_two_numbers(number_a, number_c)
	max_1_2_3 = max_of_two_numbers(max_1_2, max_1_3)
	print('наибольшее из чисел:', max_1_2_3)
	return max_1_2_3


user_index_a = input('Чему равен коэффициент a?: ')
user_index_a = float(user_index_a.replace(',', '.'))
user_index_b = input('Чему равен коэффициент b?: ')
user_index_b = float(user_index_b.replace(',', '.'))
user_index_c = input('Чему равен коэффициент b?: ')
user_index_c = float(user_index_c.replace(',', '.'))
  
max_of_three_numbers(user_index_a, user_index_b, user_index_c)
  