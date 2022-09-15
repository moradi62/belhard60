####################### List списки []
# li_1 = '0123456789'
# li_2 = '0123456789'
# aa = [a + b for a in li_1 for b in li_2 if (a != '0' and b != '0')]
# bb = [a + b for a in li_1 for b in li_2 if (a != '0' or b != '0')]
# #bb = [a + b for a in li_1 if a != '1' for b in li_2 if b != '0' ]
#cc = [a + b for a in li_1 if (a != '0' and a != '2' and a != '4' and a != '8' ) for b in li_2 if (b != '0' and b != '2' and b != '4' and b != '8' ) ]
# print(aa)
# print(bb)
#print(cc)
######################## tuple кортежи ()
# a = [1, 2, 3, 4]
# b = (1, 2, 3, 4)
# c = tuple('Mohsen Moradi')
# d = 'mohsen', 'Moradi'
# print(a.__sizeof__())
# print(b.__sizeof__())
# print(c)
# print(d)
######################## dict словари {}
#1)
# a = {1:12312, 3:234234}
# print(a[1])

# #2)
# a = dict(name='Mohsen', fam='Moradi')
# print(a['name'])

#3)
# a = dict([(1,"a"),(2,"b"),(3,"c")])
# print(a)

#4)
# a = dict.fromkeys(['a','b','c'], 'default')
# print(a)

#5)
# a = {b: b**2 for b in range(1, 8)}
# print(a)

####################### Множества (set и frozenset)
# a = set('hello')
# b = {1,2,'3'}
# print(type(a))
# print(a)
# print(type(b))
# print(b)

# a = set('hello')
# b = frozenset('qwerty')
# a.add(1)
# #b.add(1) dont work
# print(a,b)

# a = [1, 2, 3, 4, 2, 1]
# print(a)
# print(set(a))

####################### Function def
# def func(x, y):
#     res = x * y
#     return res
#def func(*args > tuple   **args > dict)

#lambda
# add = lambda x , y: 2*x+2*y
#
# print(add(2,3))
#
# print((lambda x, y: x+y)(2,5))

####################### try / except
# num1 = int(input('num1'))
# num2 = int(input('num2'))
#
# try:
#     res = num1 / num2
# except ZeroDivisionError:
#     print('oooooooo')
#     res = 0
# print(res)

# try:
#     in_ = int(input('num: '))
# except ValueError:
#     print('NOT Number')
#     in_ = 0
# else:
#     print('если не будет ошибки')
# finally:
#     print('выполняетсф 100%')
# print(in_)

######################### FILE
# f = open("test.txt")    # open file in current directory
# f = open("C:/Python38/README.txt")  # specifying full path
# f = open("test.txt")      # equivalent to 'r' or 'rt'
# f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode
# f = open("test.txt", mode='r', encoding='utf-8')
# f = open("test.txt", encoding = 'utf-8')
# perform file operations
# f.close()
# try:
#    f = open("test.txt", encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()
#
# with open("test.txt", encoding = 'utf-8') as f:
#    # perform file operations
#
# with open("test.txt", 'w', encoding='utf-8') as f:
#     f.write("my first file\n")
#     f.write("This file\n\n")
#     f.write("contains three lines\n")
#
#
# f = open('command.txt', 'r+t')
# f.write('Hi\nHELLO WORLD')
# for line in f:
#     print(line)
# f.close()
#
# a, b = input("name: ").split()
# print(a)
# print(b)

######################################
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

# data = []
# line = input('Emnter numbers: ')
# while line != '':
#     data.append(int(line))
#     line = input('Emnter numbers: ')
#
# print('All elements of list ', data)
# lenn = len(data) - 1
# buf_list_m = []
# buf_list_z = []
# for i in range(0, lenn):
#     if data[lenn - i] < 0:
#         buf_list_m.append(data.pop(lenn - i))
#     elif data[lenn - i] == 0:
#         buf_list_z.append(data.pop(lenn - i))
#
# buf_list_m.extend(buf_list_z)
# buf_list_m.extend(data)
#
# print('+ _ 0 :', buf_list_m)

##############################################
