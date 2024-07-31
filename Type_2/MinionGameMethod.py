# def hum(arr):
#     for i in range(1, len(arr)+1):
#         print(arr[:i])
#
# arr = "banana"
# hum(arr)

def kum(arr2):
    count=0
    n=len(arr2)
    for i in range(n):
        count=count+(n-i)
    print(count)
arr2 = "ABCDE"
kum(arr2)