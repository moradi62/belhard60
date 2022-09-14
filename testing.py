# matrix = [[1, 2, 3], [1, 2, 3]]
# for i in range(2):
#     for j in range(3):
#         print(matrix[i][j], end = '  ')
import setuptools

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(20)
#     left(20)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
# a = 'mohsen"s %s Moradi' %'Ali'
# S = 'sypatex'
# print("a {0} parrot".format(kind)S.find('pa'))
# print(a)
# ss = 'sdfsdfsdf' 'ghhjghj' "hjgj"
# print(ss)
# aa = [1,2,3,4,5,6,7,8,9]
# bb = []
# cc = []
# print(len(aa))
# bb.append(aa[i] for i in range(0,len(aa)-1))
# cc.__add__(aa[i] for i in range(0,len(aa)-1))
# print(bb)
# print(cc)
# num_str = '123456789'
# # aa = [a for a in num_str if (a != '0' and b != '0')]
# aa = []
# # aa.insert(1, num_str[int(j)] for i in num_str for j in range(0,len(num_str)-1))
# print(num_str[1])
# bb = aa.insert(2, num_str[3])
#
# print(aa)
# print('\x45')
# print('\u0105')
#جمع المت های لیست ###################################
# data = [0, 1, -1, 3, -4, 0]
# i,j = 0,0
# while i < len(data):
#     j = j + data[i]
#     i += 1
# print(j)
################################## append

# data = [2, 4, 4, 4, 9]
# print(data)
# data.append(5)
# print('APPEND : 5', data)
# data.insert(2, 3)
# print('INSERT 3 : ', data)
# print(data.pop(2))
# print('POP INDEX 2', data)
# data.remove(4)
# print('REMOVE 4 : ', data)
#################################### СПИСОК ДОБАВЛЕНИЕ - СОРТИРОВКА - УДАЛЕНИЕ ВЫБРОСА
# values = []
#
# line = input('Input numbers. For exit press Enter: ')
# while line != '':
#     num = int(line)
#     values.append(num)
#     line = input('Input numbers. For exit press Enter: ')
# print('Your enter list: ',values)
# print()
# line = int(input('Input numbers of remove max and min value: '))
#
# i = 1
# rem_values = []
# while i <= line:
#     rem_values.append(values.pop(values.index(max(values))))
#     rem_values.append(values.pop(values.index(min(values))))
#     i += 1
# print('Values : ', values)
# print()
# print('Removed values : ', sorted(rem_values))
#
#
# # values.sort(reverse=True)
# print('Your enter list: ',values)

# search = int(input('Enter Number for find in list: '))
# if search in values:
#     print('In list ', search, ' index is = ', values.index(search))
# else:
#     print('NOT Find ', search, ' in list')
# ######################################################## ИЗБАВЛЕНИЕ ОТ ДУБЛИКАТОВ
#
# data = []
# line = input('Emnter numbers: ')
# while line != '':
#     data.append(line)
#     line = input('Emnter numbers: ')
#
# print('All elements of list ', data)
# lenn = len(data)
# for i in range(1 ,lenn):
#     if data.count(data[lenn-i])>1:
#         data.pop(i)
# print('Dublicate removed elements of list ', data)


######################################################## ОТРИЦАТЕЛЬНЫЕ - ПОЛОЖИТЕЛЬНИЕ И НУЛЕЙ

data = []
line = input('Emnter numbers: ')
while line != '':
    data.append(int(line))
    line = input('Emnter numbers: ')

print('All elements of list ', data)
lenn = len(data) - 1
buf_list_m = []
buf_list_z = []
for i in range(0, lenn):
    if data[lenn - i] < 0:
        buf_list_m.append(data.pop(lenn - i))
    elif data[lenn - i] == 0:
        buf_list_z.append(data.pop(lenn - i))

buf_list_m.extend(buf_list_z)
buf_list_m.extend(data)

print('+ _ 0 :', buf_list_m)
