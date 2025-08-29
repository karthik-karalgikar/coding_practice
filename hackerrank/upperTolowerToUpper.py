def swap_case(s):
    result = []

    for i in s:
        if i.islower():
            result.append(i.upper())
        else:
            result.append(i.lower())

    return ''.join(result)

print(swap_case(s="DaDedDtsrT"))

'''
TRACING - 
understandable
'''