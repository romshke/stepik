# try:
#     print(all(map(lambda _: True if 0 <= _ <= 255 else False, map(int, input().split('.')))))
# except:
#     print(False)
    
    
print(all(map(lambda _: _.isdigit() and 0 <= int(_) <= 255, input().split('.'))))