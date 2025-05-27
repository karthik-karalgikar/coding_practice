'''
Write a function that takes a 2-word string and returns True if both words begin with 
the same letter
'''

def twoWordString(text):
    nums = text.lower().split()
    first = nums[0]
    second = nums[1]
    return first[0] == second[0]

text = "Hello World"
result = twoWordString(text)
print(result)
