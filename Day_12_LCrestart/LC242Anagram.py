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

def isAnagramdict(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in s:
        if i in s_to_t:
            s_to_t[i] = s_to_t[i] + 1
        else:
            s_to_t[i] = 1

    for i in t:
        if i in t_to_s:
            t_to_s[i] = t_to_s[i] + 1
        else:
            t_to_s[i] = 1

    if s_to_t == t_to_s:
        return True
    else:
        return False
    
s = "anagram"
t = "naagram"
result = isAnagramdict(s, t)
print(result)

'''
TRACING:

s = "anagram"
t = "naagram"

len(s) = 7
len(t) = 7

if len(s) != len(t) => false

s_to_t = {}
t_to_s = {}

for i in s:
    -> i = 'a'
    s_to_t[i] = s_to_t.get(i, 0) + 1
    => s_to_t['a'] = s_to_t.get('a', 0) + 1
    This means, get 0 if 'a' does not exist in s_to_t. If it exists then return its value

    So now, a does not exist. That's why 0 is returned. 

    s_to_t['a'] = 0 + 1
    s_to_t = {'a' : 1}

    -> i = 'n'
    s_to_t[i] = s_to_t.get(i, 0) + 1
    => s_to_t['n'] = s_to_t.get('n', 0) + 1 
    s_to_t['n'] = 1
    s_to_t = {'a' : 1, 'n' : 1}

    -> i = 'a'
    s_to_t[i] = s_to_t.get(i, 0) + 1
    => s_to_t['a'] = s_to_t.get('a', 0) + 1
    s_to_t['n'] = 1 + 1 (a exists, so its value(1) is returned)
    s_to_t = {'a' : 2, 'n' : 1}

    -> i = 'g'
    s_to_t[i] = s_to_t.get(i, 0) + 1
    => s_to_t['g'] = s_to_t.get('g', 0) + 1
    s_to_t['g'] = 1
    s_to_t = {'a' : 2, 'n' : 1, 'g' : 1}

    -> i = 'r'
    s_to_t[i] = s_to_t.get(i, 0) + 1
    => s_to_t['r'] = s_to_t.get('r', 0) + 1
    s_to_t['r'] = 1
    s_to_t = {'a' : 2, 'n' : 1, 'g' : 1, 'r' : 1}

    -> i = 'a'
    s_to_t[i] = s_to_t.get(i, 0) + 1
    => s_to_t['a'] = s_to_t.get('a', 0) + 1
    s_to_t['n'] = 2 + 1 (a exists, so its value(1) is returned)
    s_to_t = {'a' : 3, 'n' : 1, 'g' : 1, 'r' : 1}

    -> i = 'm'
    s_to_t[i] = s_to_t.get(i, 0) + 1
    => s_to_t['m'] = s_to_t.get('m', 0) + 1
    s_to_t['m'] = 1
    s_to_t = {'a' : 3, 'n' : 1, 'g' : 1, 'r' : 1, 'm' : 1}

for i in t: 
    -> i = 'a'
    t_to_s[i] = t_to_s.get(i, 0) + 1
    => t_to_s['n'] = t_to_s.get('n', 0) + 1
    This means, get 0 if 'n' does not exist in t_to_s. If it exists then return its value

    So now, n does not exist. That's why 0 is returned. 

    t_to_s['n'] = 1 + 1
    t_to_s = {'n' : 1}

    -> i = 'a'
    t_to_s[i] = t_to_s.get(i, 0) + 1
    => t_to_s['a'] = t_to_s.get('a', 0) + 1 
    t_to_s['a'] = 1
    t_to_s = {'n' : 1, 'a' : 1}

    -> i = 'a'
    t_to_s[i] = t_to_s.get(i, 0) + 1
    => t_to_s['a'] = t_to_s.get('a', 0) + 1
    t_to_s['n'] = 1 + 1 (a exists, so its value(1) is returned)
    t_to_s = {'n' : 1, 'a' : 1}

    -> i = 'g'
    t_to_s[i] = t_to_s.get(i, 0) + 1
    => t_to_s['g'] = t_to_s.get('g', 0) + 1
    t_to_s['g'] = 1
    t_to_s = {'n' : 1, 'a' : 2, 'g' : 1}

    -> i = 'r'
    t_to_s[i] = t_to_s.get(i, 0) + 1
    => t_to_s['r'] = t_to_s.get('r', 0) + 1
    t_to_s['r'] = 1
    t_to_s = {'n' : 1, 'a' : 2, 'g' : 1, 'r' : 1}

    -> i = 'a'
    t_to_s[i] = t_to_s.get(i, 0) + 1
    => t_to_s['a'] = t_to_s.get('a', 0) + 1
    t_to_s['n'] = 2 + 1 (a exists, so its value(1) is returned)
    t_to_s = {'n' : 1, 'a' : 3, 'g' : 1, 'r' : 1}

    -> i = 'm'
    t_to_s[i] = t_to_s.get(i, 0) + 1
    => t_to_s['m'] = t_to_s.get('m', 0) + 1
    t_to_s['m'] = 1
    t_to_s = {'n' : 1, 'a' : 3, 'g' : 1, 'r' : 1, 'm' : 1}

Order doesn't matter in dictonaries, only the key and value pairs are compared to check if they are same

s_to_t = {'a' : 3, 'n' : 1, 'g' : 1, 'r' : 1, 'm' : 1}
t_to_s = {'n' : 1, 'a' : 3, 'g' : 1, 'r' : 1, 'm' : 1}

if s_to_t == t_to_s:
    return True
else:   
    return False


Output = True





    
    
'''