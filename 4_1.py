#Заполнить список степенями числа 2 (от 2^1 до 2^n)

inp_num = int(input('Enter number: '))

lis = []

for i in range(1, inp_num+1):
    lis.append(2**i)

print(lis)