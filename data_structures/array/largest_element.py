import sys

def largest(arr):
    largest_num = -sys.maxsize
    for i in arr:
        if i > largest_num:
            largest_num = i
    print(largest_num)

arr = [1,2,3,4,5,6,7,8,2,4,5,7,34,56,23,1234,134,57,67,345]

largest(arr)
