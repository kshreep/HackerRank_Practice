if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        students.append([input(), float(input())])

    second_lowest = sorted(set(marks for name, marks in students))[1]
    print('\n'.join([name for name, marks in sorted(students) if marks == second_lowest]))

