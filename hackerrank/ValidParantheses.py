# def areBracketsProperlyMatched(code_snippet):
#     # stack = []
#     brackets = ["(", ")", "[", "]", "{", "}"]
#     code_snippet = list(code_snippet)
    
#     # for i in code_snippet:
#     #     if i in brackets:
#     #         stack.append(i)
    
#     frequency = {}
    
#     for i in code_snippet:
#         if i in brackets:
#             if i in frequency:
#                 frequency[i] = frequency[i] + 1
#             else:
#                 frequency[i] = 1
                
#     for i in frequency:
#         if frequency[i] % 2 == 0:
#             return True
#         else:
#             return False

def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    stack = []
    
    for i in code_snippet:
        if i in "({[":
            stack.append(i)
        elif i in ")}]":  
            if len(stack) == 0:
                return False 
            top = stack.pop()
            if (i == ")" and top != "(") or (i == "}" and top != "{") or (i == "]" and top != "["):
                return False
    
    return len(stack) == 0
        
print(areBracketsProperlyMatched(code_snippet="{[()]}"))

'''
TRACING :

code_snippet = "{[()]}"

stack = []

for i in code_snippet:
    -> i = "{"
    if i in "({[":
        stack.append(i)

        stack = ["{"]

    -> i = "["
    if i in "({[":
        stack.append(i)

        stack = ["{", "["]

    -> i = "("
    if i in "({[":
        stack.append(i)

        stack = ["{", "[", "("]

    -> i = ")"
    elif i in ")}]":
        if len(stack) == 0 -> false

        top = '('
        top = stack.pop()

        stack = ["{", "["]

        if (i == ")" and top != "(") or (i == "}" and top != "{") or (i == "]" and top != "["):
        i == ')' and top != '(' -> false
        the other two also false , so its 0 or 0 or 0 -> 0

    -> i = "]"
    elif i in ")}]":
        if len(stack) == 0 -> false

        top = '['
        top = stack.pop()

        stack = ["{"]

        if (i == ")" and top != "(") or (i == "}" and top != "{") or (i == "]" and top != "["):
        i = ']' and top != '[' -> false
        the other two also false

    -> i = "}"
    elif i in ")}]":
        if len(stack) == 0 -> false

        top = '{'
        top = stack.pop()

        stack = []

        if (i == ")" and top != "(") or (i == "}" and top != "{") or (i == "]" and top != "["):
        i = '}' and top = '{' -> false
        the other two are also false

return len(stack) == 0

len(stack) == 0 -> True

Output = True

'''