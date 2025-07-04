import json

def plusOne(digits):
    # if digits[-1] != 9:
    #     digits[-1] = digits[-1] + 1
    # else:
    #     for i in range(len(digits[::-1])):
    #         carry = 1
    #         digits[i - 1] = digits[i - 1] + carry

    s = ''
    for i in range(len(digits)):
        s = s + str(digits[i])

    s = int(s)
    s = s + 1
    s = str(s)
    # a = list(s)
    result = []

    for i in s:
        result.append(json.loads(i))
        
    return result

print(plusOne(digits=[4, 2, 3, 1]))