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

a, b = input("name: ").split()
print(a)
print(b)