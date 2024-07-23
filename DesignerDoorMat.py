def generate_door_mat(X, width):
    X = int(X)
    width = int(width)

    for i in range(1, X, 2):
        pattern = '.|.' * i
        print(pattern.center(width, '-'))
    print('WELCOME'.center(width, '-'))
    for i in range(X - 2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(width, '-'))


# Read input from a single line
X, width = map(int, input().split())
generate_door_mat(X, width)
