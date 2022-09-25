# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

from random import randint


def sum_lst(lst: list)->list:
    buff_lst = []
    buff_lst.append(lst[0]+lst[1]) # index = 0
    for ind in range(1, len(lst)-1): # index 1 ~ n-1
        buff_lst.append(lst[ind-1]+lst[ind+1])
    buff_lst.append(lst[-2]+lst[-1])
    return buff_lst

lst = []
for i in range(10):
    lst.append(randint(0, 10))

print(lst)

print(sum_lst(lst))

