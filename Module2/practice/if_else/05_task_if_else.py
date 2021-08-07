# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here
m = int(input('enter number: '))
if m >= 3 and m <= 5:
	print('Spring')
elif m > 5 and m <= 8:
	print('Summer')
elif m > 8 and m <= 11:
	print('Autumn')
else:
	print('Winter is coming')
