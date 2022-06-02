# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
# 
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
# 
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
# 
# A = KS
# 
# K = i(1 + i) ** n / (1 + i) ** n - 1
# 
# Пример:
# 
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
# 
# Период: 1
# 
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
# 
# 
# Период: 2
# 
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
# 
# Период: 3
# 
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
# 
# Остаток долга: 17409632.774728
# 
# =================================================
# 
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
# 
# Период: 1
# 
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
# 
# Период: 2
# 
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
# 
# Период: 3
# 
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
# 
# Период: 4
# 
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
# 
# Остаток долга: 0.017039266414940357


# A = KS
# 
# K = i(1 + i) ** n / ((1 + i) ** n - 1)

def year_annuity_payment(loan, percent, years_quantity):
	percent = percent / 100
	coef = percent * (1 + percent) ** years_quantity / ((1 + percent) ** years_quantity - 1)
	payment = round(loan * coef, 2)
	total_payment = loan * coef * years_quantity
	year = 0
	
	while years_quantity > 0:
		if year == 3:
			add_years_quantity = int(input('\nНа сколько лет продлевается договор: '))
			add_percent = int(input('На сколько увеличивается процент: '))
			add_percent = add_percent / 100
			years_quantity = years_quantity + add_years_quantity
			percent = percent + add_percent
			coef = percent * (1 + percent) ** years_quantity / ((1 + percent) ** years_quantity - 1)
			payment = round(loan * coef, 2)
		year_debt = loan * percent
		year_loan_body = payment - year_debt
		loan = loan - year_loan_body
		year += 1
		print('\nИдёт ', year, 'й год платежей', end = '')
		print('\nУплачено процентов за год:', round(year_debt, 2))
		print('Погашённое тело долга за год:', round(year_loan_body, 2))
		print('Оставшееся тело долга', round(loan, 2))
		years_quantity -= 1
	print('Всего уплачено:', round(total_payment, 2))
		
	
loan_sum = input('Введите сумму кредита: ')
loan_sum = float(loan_sum.replace(',', '.'))
loan_years = int(input('На сколько лет берётся кредит: '))
loan_percent = int(input('Какой процент годовых: '))
 
year_annuity_payment(loan_sum, loan_percent, loan_years)
	

	
	
	
	
	
	
	
	
	
	
	
	
	