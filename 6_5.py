# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def my_rev(lst):
    # temp = 0
    for i in range(0, (len(lst)//2)+1):
        temp = lst[i]
        lst[i] = lst[-1-i]
        lst[-1-i] = temp
    return lst


lst = [1, 2, 3 , 4 ,5]
print(my_rev(lst))

