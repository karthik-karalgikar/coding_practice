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

'''
TRACING :

s = "A man, a plan, a canal: Panama"
s = s.lower()
=> s = "a man, a plan, a canal: panama"

cleaned = []

for i in s:
    -> i = a
    if i.isalnum() -> checks if it is anything but letters or numbers -> if not, then ut is true and goes inside
    statement
        cleaned.append(i) 
        => cleaned = ['a']

    -> i = ''
    if i.isalnum() -> yes

    -> i = 'm'
    if i.isalnum():
        cleaned.append(i)
        => cleaned = ['a', 'm']

    -> i = 'a'
    if i.isalnum():
        cleaned.append(i)
        => cleaned = ['a', 'm', 'a']

    -> i = 'n'
    if i.isalnum():
        cleaned.append(i)
        => cleaned = ['a', 'm', 'a', 'n']

    -> i = ','
    if i.isalnum() -> yes

    -> i = ''
    if i.isalnum() -> yes

    -> i = 'a'
    if i.isalnum():
    cleaned.append(i)
    => cleaned = ['a', 'm', 'a', 'n', 'a']

    -> i = ''
    if i.isalnum() -> yes
    .
    .
    .
    .
    .
    .
    .
    cleaned = ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']

    if cleaned == cleaned[::-1]:
        return True
    else:
        return False

    Output = True

'''

