# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

dic = {}
inp_num = int(input('Вводите количество элементов :'))

for elements in range(0, inp_num):
    elm_name = input('Вводите Имя элемента: ')
    elm_email = input('Вводите email элемента: ')
    dic[elements] = [elm_name, elm_email]
    print()

print(dic.items())

#2###################################
n = int(input())
users = {i: {'name:': input(), 'email: ': input()} for i in range(0,n)}
print(users)



