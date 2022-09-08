# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

num_1 = input('Number 1: ')
num_2 = input('Number 2: ')
num_3 = input('Number 3: ')

res_zero = int(num_1) !=0
res_minus = int(num_1.startswith('-') + num_2.startswith('-') + num_3.startswith('-'))-res_zero
res_plus = 3 - int(res_minus)

print('Количество отрицательных чисел: ', res_minus)
print('Количество положительных чисел: ', res_plus)
print('Количество 0: ', res_zero)

#Второй вариант
num_1 = float(input('Number 1: '))
num_2 = float(input('Number 2: '))
num_3 = float(input('Number 3: '))

res_zero = (num_1 == 0) + (num_2 == 0) + (num_3 == 0)
res_plus = (num_1 > 0) + (num_2 > 0) + (num_3 > 0)
res_minus = 3-res_plus-res_zero

print('Количество отрицательных чисел: ', res_minus)
print('Количество положительных чисел: ', res_plus)
print('Количество 0: ', res_zero)
