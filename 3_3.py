# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

inp_name = input('Please enter your Name: ').strip().capitalize()
inp_age = input('Please enter your age: ').strip()
inp_city = input('Please enter your city: ').strip().upper()

#Первый вариант
res_1 = 'Меня зовут ' + inp_name + '\nЯ из города ' + inp_city + '.\nМне ' + inp_age + ' лет.'
print(res_1, '\n')

#Второй вариант
res_2 = 'Меня зовут {name}.\nЯ из города {city}.\nМне {age} лет.'.format(name=inp_name,city=inp_city,age=inp_age)
print(res_2, '\n')

#Третий вариант
res_3 = f'Меня зовут {inp_name}.\nЯ из города {inp_city}.\nМне {inp_age} лет.'
print(res_3)