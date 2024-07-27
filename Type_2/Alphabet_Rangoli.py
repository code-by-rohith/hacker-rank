# You are given an integer,N . Your task is to print an alphabet rangoli of size N .
# (Rangoli is a form of Indian folk art based on creation of patterns.)
# Sample Input
#
# 5
# Sample Output
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(n):

    import string
    alphabet = string.ascii_lowercase[:n]
    width = 4 * n - 3
    lines = []
    for i in range(n):
        left_part = alphabet[n-1:i:-1]
        right_part = alphabet[i:n]
        line = '-'.join(left_part + right_part)
        lines.append(line.center(width, '-'))
    full_pattern = '\n'.join(lines[::-1] + lines[1:])
    print(full_pattern)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)