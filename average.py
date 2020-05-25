n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

print(student_marks)

req = input("enter name")


avg = (student_marks[req][0] + student_marks[req][1] + student_marks[req][2])/3

print("%.2f"%avg)
