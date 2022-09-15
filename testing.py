# str1 = list(input('Enter word 1: '))
# str2 = list(input('Enter word 2: '))
#
# lee = 0
# for i in str1:
#     if i in str2:
#         str2.remove(i)
#         lee += 1
#         #print(str2)
#     else:
#         break
# if lee == len(str1):
#     print('Anagrama')


# te = 0
# inp = input('Enter word: ')
# i = 0
# while i < len(inp) - 1:
#     if inp(i) == inp(i+1):
#         te += 1
#         i += 2
#     else:
#         i += 1
# print (te)
#


# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# day = 1
# protcent = 0.10
# while x < y:
#     x += x * protcent   # or x *= 1.1
#     day += 1
# print(day)
##########################################################

from random import randint

n = randint(0, 100)
print(n)
pit = 1

x = int(input('Enter x: '))
while x != n:
    if x > n: print(' n < x ')
    if x < n: print(' n > x ')
    x = int(input('Enter x: '))
    pit += 1
print(pit)
