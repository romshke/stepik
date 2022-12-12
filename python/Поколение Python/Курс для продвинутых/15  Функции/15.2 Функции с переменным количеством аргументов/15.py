def info_kwargs(**kwargs):
    print(*sorted(f'{item[0]}: {item[1]}' for item in kwargs.items()), sep='\n')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 