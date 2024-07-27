if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        line = input().split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_marks[name] = marks

    query_name = input()


    query_marks = student_marks[query_name]
    average = sum(query_marks) / len(query_marks)

    print(f"{average:.2f}")
