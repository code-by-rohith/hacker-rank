def wrap(string, max_width):
    if not string:
        return ''
    line = string[:max_width]
    return line + '\n' + wrap(string[max_width:], max_width)

string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

print(wrap(string, max_width))
