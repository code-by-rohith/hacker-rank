def generate_door_mat(X, width):
    for i in range(1, X, 2):
        pattern = '.|.' * i
        print(pattern.center(width, '-'))
    print('WELCOME'.center(width, '-'))
    for i in range(X - 2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(width, '-'))

X = 9
width = 27
generate_door_mat(X, width)
