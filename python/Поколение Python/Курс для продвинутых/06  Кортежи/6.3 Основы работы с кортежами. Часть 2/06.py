poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
tmp = list(poet_data)
tmp[-1] = 'Москва'
poet_data = tuple(tmp)
print(poet_data)