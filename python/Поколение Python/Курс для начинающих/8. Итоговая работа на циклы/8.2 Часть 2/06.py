n = input()
count_3, count_last, count_even, sum_of_digits_greater_than_5, mul_of_digits_greater_than_7, count_0_and_5 = 0, 0, 0, 0, 1, 0

for i in n[::]:
    if int(i) == 3: count_3 += 1
    if int(i) == int(n[-1]): count_last += 1
    if int(i) % 2 == 0: count_even += 1
    if int(i) > 5: sum_of_digits_greater_than_5 += int(i)
    if int(i) > 7: mul_of_digits_greater_than_7 *= int(i)
    if int(i) == 0 or int(i) == 5: count_0_and_5 += 1
print(count_3, count_last, count_even, sum_of_digits_greater_than_5, mul_of_digits_greater_than_7, count_0_and_5, sep='\n')