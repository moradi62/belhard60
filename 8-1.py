text = """
Mobil telephone 3000

ru от 1 шт. 18000

ru от 5 шт. 18000

en от 5 шт. 17000
"""


def list_dict(lst: list) -> dict:
    dct = {}
    dct[lst[0]] = [lst[1]+lst[2], lst[3]+lst[4]]
    return dct

countries = ['ru', 'en', 'fr']
from_price = ['от 1', 'от 5', 'от 20', 'от 50']
buf = ''
buf_title = ''
title = False
semiclon = ';'

for i in text:
    if i != '\n':
        buf += i
        semiclon = ';'

    else:
        if not title:
            if buf:
                buf_title = buf.strip(';')
                buf = ''
                title = True

        if semiclon:
            buf += ';'
            semiclon = ''

buf = buf.strip(';')
buf = buf.split(';')

buf2 = ''
list_buf = []
for i in buf:
    buf2 = i.split()
    list_buf.append(buf2)

dct = []
for i in list_buf:
    dct.append(list_dict(i))

print('Title = ', buf_title , 'len = ', len(buf_title))
print(dct)
