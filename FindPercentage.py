if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}  # Dictionary to store student records

    for _ in range(n):
        line = input().split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_marks[name] = marks

    query_name = input()  # Name of the student to query

    # Calculate the average of the marks
    query_marks = student_marks[query_name]
    average = sum(query_marks) / len(query_marks)

    # Print the average with 2 decimal places
    print(f"{average:.2f}")
