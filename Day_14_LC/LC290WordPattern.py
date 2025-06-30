#Similar to 205:

def wordPattern(pattern, s):
    flag = 0
    a = s.split()
    if len(pattern) != len(a):
        return False
    
    elif len(pattern) == len(a):
        for i in range(len(pattern)):
            if pattern.index(pattern[i]) != a.index(a[i]):
                flag = 1

    if flag == 1:
        return False
    else:
        return True
  
pattern = "abba"
s = "dog cat cat dog" 
result = wordPattern(pattern, s)
print(result)

'''
TRACING : 

Refer 205

'''