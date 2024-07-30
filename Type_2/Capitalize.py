def fun(str_list):
    result = ""
    for i in str_list:
        if len(i) > 0:
            i = i[0].upper() + i[1:]
        result += i+" "
    return result

input_str = "hi bay"

str_list = input_str.split()

result = fun(str_list)

print(result)
