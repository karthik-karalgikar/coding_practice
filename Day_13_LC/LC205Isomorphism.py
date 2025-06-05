def isIsomorphic(s, t):
    flag = 0
    if len(s) == len(t):
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                flag = 1
        
    if flag == 1:
        return False
    else:
        return True

a = "kak"
b = "add"
result = isIsomorphic(a, b)
print(result)

'''
TRACING :

a = "kak"
b = "add"

flag = 0

if len(a) == len(b):
    len(a) = 3, len(b) = 3 -> true
    inside if statement:
        for i in range(len(a)) -> range(3) -> until 2:
        i = 0
            if a.index(a[i]) != b.index(b[i]):
                => a.index(a[0]) = a.index("k") -> 0
                => b.index(b[0]) = b.index("a") -> 0

                0 == 0, true -> does not go inside if statement.

        i = 1
            if a.index(a[i]) != b.index(b[i]):
                => a.index(a[1]) = a.index("a") -> 1
                => b.index(b[1]) = b.index("d") -> 1

                1 == 1, true -> does not go inside if statement.

        i = 2
            if a.index(a[i]) != b.index(b[i]):
                => a.index(a[2]) = a.index("k") -> 0
                => b.index(b[2]) = b.index("d") -> 1

                0 != 1, true -> goes inside if statement.

                flag = 1

if flag == 1:
    return False
else:
    return True
'''

def isIsomorphic2(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i, j in zip(s, t):
        print(i, j)
        if (i in s_to_t and s_to_t[i] != j):
            return False
        
        if (j in t_to_s and t_to_s[j] != i):
            return False
        
        s_to_t[i] = j
        t_to_s[j] = i

    return True

s = "kak"
t = "add"
result2 = isIsomorphic2(s, t)
print(result2)

'''
TRACING :

s = "kak"
t = "add"
len(s) = 3
len(t) = 3

s_to_t = {}
t_to_s = {}

for i, j in zip(s, t):
    zip(s, t) -> ('k', 'a')
                 ('a', 'd')
                 ('k', 'd')
    
    i = k, j = a
        
    if (i in s_to_t and s_to_t[i] != j):
        k in s_to_t -> false, s_to_t is empty.

    if (j in t_to_s and t_to_s[j] != i):
        a in t_to_s -> false, t_to_s is empty.

    s_to_t[i] = j -> s_to_t[k] = a
    t_to_s[j] = i -> t_to_s[a] = k

    s_to_t = {'k' : 'a'}
    t_to_s = {'a' : 'k'}

    i = a, j = d

    if (i in s_to_t and s_to_t[i] != j):
        a in s_to_t -> false, s_to_t has only k and a

        (need to check if it checks both the key and value)

'''