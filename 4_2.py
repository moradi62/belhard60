# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

# alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
#          '0','1','2','3','4','5','6','7','8','9'}
dict = {}
words = input('Enter your text: ')

# for i in alpha:
#     if words.count(i) > 0: print('Количества вхождений буква ', i, 'в тексте = ', words.count(i))

for i in words:
    if i == ' ':
        continue
    dict[i] = words.count(i)
print('Словарь вхождении буква :\n', dict)