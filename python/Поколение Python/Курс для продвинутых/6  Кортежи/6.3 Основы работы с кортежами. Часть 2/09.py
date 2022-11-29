n = int(input())
students = []
good_marks_students = []

for _ in range(n):
    students.append(input())
    if int(students[_][-1]) > 3:
        good_marks_students.append(students[_])
        
for _ in students:
    print(_)
    
print()

for _ in good_marks_students:
    print(_)