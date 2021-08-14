# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
new_list = [-9, -5, -1, 3, 8]
sum = 0
for element in new_list:
    if element > 0:
        sum += element
print(sum)
