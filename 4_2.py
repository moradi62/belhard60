# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

dic = {}

words = input('Enter your text: ').islower()

for i in words:
    if i == ' ':
        continue
    dic[i] = words.count(i)

print('Словарь вхождении буква :\n', dic)