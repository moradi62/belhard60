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

a = [1, 2, 3, 4, 2, 1]
print(a)
print(set(a))
