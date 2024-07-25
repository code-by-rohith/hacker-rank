
def mutate_string(s,i,c):
    list1=list(s)
    print(list1)
    list1[i]=c
    string1="".join(list1)

    return string1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)