# Input - [1,2,3,4,[5,6,7,8],[9,10]]
# Output - [1,2,3,4,5,6,7,8,9,10]

#0. Create an empty list: flat
#1. Iterate through all elements checking if there is a list using "isinstance(,type)
#2. if element is not a list: APPENDS it to flat list
#3 if element is a list: EXTEND it with found list

lst = [1,2,3,4,[5,6,7,8],[9,10]]

flat = []

def flatten(lst):
  for sub in lst:
    if isinstance(sub, list):
      flat.extend(sub)
    else:
      flat.append(sub)

  print(flat)
  
first=[1,2,3]
second=[4,5,6]
third=second+first
print(third)
print(flatten(lst))