# Q - Find a number in the array such that all the elements
# in the array are divisible by it

# A - just find the min in the array and check if all the other elements
# are divisble by it

import sys

def check(arr):
    min = sys.maxsize #max int size
    for i in arr: #determine min
        if i < min:
            min = i
    for i in arr: #compare min with all numbers
        if not i % min == 0:
            return False
    return True


arr = [20,10,15,5,100,200, 201]

print(check(arr))
