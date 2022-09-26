# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

from random import randint

def sum_num(lst:list) -> list:
    res_lst = []
    for ind in range(0, len(lst)):
        if ind == 0:
            res_lst.append(lst[-1] + lst[1])
        elif ind == len(num_lst) - 1:
            res_lst.append(lst[0] + lst[-2])
        else:
            res_lst.append(lst[ind - 1] + lst[ind + 1])
    return res_lst

num_lst = []

for rnd in range(0,10):
    num_lst.append(randint(0, 10))

print('список рандомных чисел')
print(num_lst)
print('сумма крайних чисел')
print(sum_num(num_lst))




