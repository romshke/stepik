s = input()

def delete_zeros(string):
    return string[string.find(list(_ for _ in string if _ != '0')[0]):]

print(delete_zeros(s[::-1]) if len(s) == 5 else s[0] + s[:0:-1])