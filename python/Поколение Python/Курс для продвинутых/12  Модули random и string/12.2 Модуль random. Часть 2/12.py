# from random import choice, randint

# n = int(input())
# students = []
# friend_list = {}

# for student in range(n):
#     students.append(input())

# lb = randint(1, n - 1)

# friends = students[lb:] + students[:lb]

# print(*(f'{student} - {friend}' for student, friend in zip(students, friends)), sep='\n')

from random import choice

students = []
friend_list = {}

for student in range(int(input())):
    students.append(input())

for student in students.copy():
    if students == student:
        friend_list[student], friend_list[friend] = friend_list[friend], student
    else:
        friend = choice([_ for _ in students if _ != student and _ not in friend_list])
        friend_list.setdefault(friend, student)
        students.remove(friend)
    
print(*(f'{student} - {friend}' for student, friend in friend_list.items()), sep='\n')