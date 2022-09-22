#Дан список чисел и на вход поступает число N, необходимо сместить список на
#указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def replace_list(lst: list, n=0):
    result = []
    if n > 0:
        result = lst[n+1:-1] + lst[0:n+1]
        return result
    else:
        return lst




my_list = [1,2,3,4,5,6,7]
num_ch = int(input('Количество перемещении: '))
print(replace_list(my_list, num_ch))



