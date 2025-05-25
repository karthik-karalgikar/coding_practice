def ivyBrackets(s):
    openCloseMapping = {"(":")", "{":"}", "[":"]"}
    stack = []
    for char in s:
        if char in '{([':
            stack.append(char)
        elif len(stack) == 0 or char != openCloseMapping[stack.pop()]:
            return 0
    return 0 if stack else 1

s = '{()}[['
print(ivyBrackets(s))

