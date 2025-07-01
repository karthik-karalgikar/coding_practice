def isHappy(n):

    visit = set()

    def get_next_number(n):
        output = 0
        while n:
            digit = n % 10
            output = output + digit * digit
            n = n // 10

        return output
    
    while n not in visit:
        visit.add(n)
        n = get_next_number(n)
        if n == 1:
            return True
       
    return False

n = 2
result = isHappy(n)
print(result)


'''
TRACING

n = 19

visit = set() 
visit = {}

while n not in visit:
    while 19 not in {} -> true
    visit.add(n) -> visit = {19}
    n = get_next_number(n) -> n = get_next_number(19)

    get_next_number(19):
        output = 0
        while n: (while n is true(19))
            digit = n % 10 -> 19 % 10 -> 9
            digit = 9
            output = output + digit * digit
            output = 0 + 9 * 9 -> 0 + 81
            output = 81
            n = n // 10 -> 19 // 10
            n = 1

        while n: (while n is true(1))
            digit = n % 10 -> 1 % 10 -> 1
            digit = 1
            output = output + digit * digit
            output = 81 + 1 * 1
            output = 82
            n = n // 10 -> 1 // 10
            n = 0

        while n: (n = 0, false)

        return output 
        output = 82

    

'''