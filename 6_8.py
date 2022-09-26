# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

country = {'Belarus':['Minsk', 'Grodno', 'Vitebsk', 'Brest', 'Mogiliev'],
           'USA':['NY', 'LA', 'Chicago', 'California'],
           'Japan':['Yokohama', 'Osaka', 'Nagoya']}

src = input('Search your City: ')

for k, v in country.items():
    if src in v:
        print(f'{k}')



