'''
You are given an array of characters letters that is sorted in non-decreasing order, 
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.
'''

def nextGreatestLetter(letters, target):
       
        for i in letters:
            if i > target:
                return i

        return letters[0]

letters = ["a", "b", "x"]
target = "a"
result = nextGreatestLetter(letters, target)
print(result)