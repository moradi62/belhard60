# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

num_1 = input('Number 1: ')
num_2 = input('Number 2: ')
num_3 = input('Number 3: ')

res_minus = num_1.startswith('-') + num_2.startswith('-') + num_3.startswith('-')
res_plus = 3 - res_minus

print('Количество отрицательных чисел: ', res_minus)
print('Количество положительных чисел: ', res_plus)
