with open('ledger.txt') as file:  
    print('$' + str(sum(map(lambda _: int(_.replace('$', '')), file.readlines()))))
    