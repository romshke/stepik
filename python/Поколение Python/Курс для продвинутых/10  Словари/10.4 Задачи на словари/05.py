countries_and_cities = {}

for _ in range(int(input())):
    words = input().split()
    countries_and_cities.setdefault(words[0], words[1:])

for _ in range(int(input())):
    city = input()
    
    for _ in countries_and_cities.items():
        if city in _[1]:
            print(_[0])