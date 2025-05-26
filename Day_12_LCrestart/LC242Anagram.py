def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    a = list(s)
    b = list(t)
    if sorted(a) == sorted(b):
        return True
    else:
        return False

s = "anagram"
t = "naagram"
result = isAnagram(s, t)
print(result)


#Difference between sort() and sorted()
'''
sort() — In-place Sort (For Lists Only)
Modifies the list in place
Returns None
Only works with lists

nums = [3, 1, 2]
nums.sort()

print(nums)  # [1, 2, 3]
print(nums.sort())  # None
nums.sort() returns None, so don't try to assign it or compare it directly.

sorted() — Returns a New Sorted List
Does NOT modify the original
Works with any iterable (e.g., strings, tuples, dictionaries)
Returns a new sorted list

nums = [3, 1, 2]
sorted_nums = sorted(nums)

print(nums)        # [3, 1, 2]   ← original unchanged
print(sorted_nums) # [1, 2, 3]



Use sort() when:
You want to modify the original list to save memory.

Use sorted() when:
You need the original list/iterable unchanged.
You're working with other iterable types (like strings or tuples).
'''