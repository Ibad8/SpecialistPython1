# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов

random_list = []
for i in range(10):
    random_list.append(random.randint(-20,20))
print(random_list)

for i in random_list:
    if i < 10:
        num_less_ten += 1
    if i > 0:
        positive_sum += i
    if i % 2 == 0:
        even_list.append(i)
try:
    avg_even = sum(even_list) / len(even_list)
except:
    print('no even numbers')

print('num_less_ten:', num_less_ten)
print('positive_sum:', positive_sum)
print('avg_even:', avg_even)
