if __name__ == '__main__':
    students = [(input(), float(input())) for x in range(int(input()))]

students = sorted(students, key=lambda x: (x[1], x[0]))

ss = None
for i,n in enumerate(students):
    if students[i][1] != students[0][1] and not ss:
        ss = students[i][1]
    if students[i][1] == ss:
        print(students[i][0])
