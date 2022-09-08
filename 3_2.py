# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3


num_1 = float(input('Number 1: '))
num_2 = float(input('Number 2: '))
num_3 = float(input('Number 3: '))
res = (num_1 + num_2 + num_3)/3

#Первый вариант
print("{:.3f}".format(res))

#Второй вариант
print(round(res, 5)) #c round не покажет несколько нулей после запетой
