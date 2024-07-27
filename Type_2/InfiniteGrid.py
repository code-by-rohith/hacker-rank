# Assume there exists infinite grid, you’re given initial position x, y.
# Inputs will be movements either L or R or U or D. After n inputs,
# you need to give the current position.
# •	Input:
# •	4 5 //initial position x, y
# •	9 //number of movements
# •	U L R R D D U L R //7 movements
# •	Output:
#      5 5

def after_movements(movements, x, y):
    for move in movements:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1

    print("The final position is", x, y)

movements = "ULRRDDULR"
x = 4
y = 5
after_movements(movements, x, y)
