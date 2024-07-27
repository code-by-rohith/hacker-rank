def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result

input_string = input()
print(split_and_join(input_string))
