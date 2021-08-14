# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

# TODO: your code here
max_len = None
for fruit in fruits:
    letters = len(fruit)
    if max_len is None or letters > max_len :
        max_len = letters
print(max_len)

n = 1

for fruit in fruits:
    if len(fruit) == max_len:
        print(n,'.',fruit)
        n+=1
    else:
        print(n,'.',' ' * (max_len - len(fruit)-1), fruit)
        n+=1
# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
