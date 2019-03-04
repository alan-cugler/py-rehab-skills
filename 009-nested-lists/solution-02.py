if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

students = sorted(students, key=lambda x: (x[1], x[0]))
student = []

for i in range(len(students)):
    if students[i][1] != students[0][1]:
        student.append(students[i])

for i in range(len(student)):
    if student[i][1] == student[0][1]:
        print(student[i][0])
