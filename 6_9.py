# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
#
def check_dict(dic: dict):
    if dic['email'] == '':
        return True
    else:
        return False

users = {}
# user = {}
for ind in range(0, 2):
    users[ind] = dict(name=input('Name: '), surname=input('Surnamee: '),
                                      tel=int(input('Tel: ')), email=input('Email: '))


for k,v in users.items():
    if check_dict(v):
        print(f'У пользователя {k} по имени {v["name"]} поле: EMAIL пуста')

