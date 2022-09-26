# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

from random import randint

def odd_num(i: int):
    return (i % 2)

def even_num(i: int):
    return (i+1) % 2

def even_odd_sort(lst: list):
    # lst.sort()
    lst_odd = list(filter(lambda ind: odd_num(ind), lst))
    lst_even = list(filter(lambda ind: even_num(ind), lst))
    return (lst_even + lst_odd)

lst = []
for i in range(10):
    lst.append(randint(0, 10))

print('список рандомных чисел')
print(lst)
print()
print('сначала четные, потом нечётные')
print(even_odd_sort(lst))
