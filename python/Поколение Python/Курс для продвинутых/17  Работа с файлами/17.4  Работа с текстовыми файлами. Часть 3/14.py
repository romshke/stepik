with open('logfile.txt') as logfile, open('output.txt', 'w') as output:  
    print(
        *list(
            _[0] for _ in list(
                map(
                    lambda _: [_[0], list(map(int, _[1].split(':'))), list(map(int, _[2].split(':')))],
                    map(lambda _: _.replace('\n', '').split(', '), logfile.readlines()) 
                )
            ) if (_[2][0] - _[1][0]) * 60 + _[2][1] - _[1][1] >= 60 
        ), 
        sep='\n',
        file=output
    )