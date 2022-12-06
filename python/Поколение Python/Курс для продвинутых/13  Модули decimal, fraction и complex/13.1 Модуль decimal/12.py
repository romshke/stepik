from decimal import *
num = Decimal(input())

print(max(num.as_tuple()[1]) + min(num.as_tuple()[1]) if len(num.as_tuple()[1]) > abs(num.as_tuple()[2]) else max(num.as_tuple()[1]))