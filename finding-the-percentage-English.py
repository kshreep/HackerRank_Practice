if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = [student_marks[name] for name in student_marks if name == query_name]
    for i in marks:
      s = sum(i)
    avg = s/float(3)
    print(f'{avg:.2f}')

# marks = student_marks[query_name]
# print(f'{sum(marks)/len(marks):.2f})