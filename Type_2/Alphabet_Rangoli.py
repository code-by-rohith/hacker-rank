def rangoli(size):
    import string
    alphabet = string.ascii_lowercase[:size]
    width = 4 * size - 3
    lines = []
    for i in range(size):
        left_part = alphabet[size-1:i:-1]
        right_part = alphabet[i:size]
        line = '-'.join(left_part + right_part)
        lines.append(line.center(width, '-'))
    full_pattern = '\n'.join(lines[::-1] + lines[1:])
    return full_pattern



print(rangoli(5))
