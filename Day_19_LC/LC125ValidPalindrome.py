def isPalindrome(s):
        
    # s = s.lower()
    # b = list(s)
    # c = []
    # # d = [':', ',','*','@','!','#','$','%','^','&','(',')']

    # for i in b[::-1]:
    #     if i.isalnum():
    #         c.append(i)

    # if c == c[::-1]:
    #     return True
    # else:
    #     return False

    s = s.lower()
    cleaned = []
    for i in s:
        if i.isalnum():
            cleaned.append(i) 
        
    return cleaned == cleaned[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))