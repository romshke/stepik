def read_csv():
    with open('data.csv') as file:
        keys = file.readline().split(',')
        data = [{key.strip(): value.strip() for key, value in zip(keys, line.split(','))} for line in file]
            
    return data

print(read_csv())