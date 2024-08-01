for i in range(1,int(input())+1):

    print(int(''.join(str(j) for j in list(range(1, i)) + list(range(i, 0, -1)))))


