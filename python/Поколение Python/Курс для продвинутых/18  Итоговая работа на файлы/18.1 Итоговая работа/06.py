with open(input()) as file1, open('forbidden_words.txt') as file2:  
    f1 = file1.read()
    f2 = file2.read().split()
    result = f1
    
    for _1 in f1.split():
        for _2 in f2:
            if _2 in _1.lower():
                lb = _1.lower().find(_2)
                result = result.replace(_1[lb:lb + len(_2)], '*' * len(_2))
                
    print(result)