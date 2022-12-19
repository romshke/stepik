def pretty_print(data, side='-', delimiter='|'):
    s = ''.join(str(f'{delimiter} {_} ') for _ in data) + delimiter
    print(' ' + side*(len(s) - 2))
    print(s)
    print(' ' + side*(len(s) - 2))

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')