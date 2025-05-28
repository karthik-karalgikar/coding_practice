def isIsomorphic(s, t):
    flag = 0
    if len(s) == len(t):
        for i in range(len(s)):
            print(s.index(s[i]))
            print(t.index(t[i]))
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