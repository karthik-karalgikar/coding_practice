def armstrong(x):
    sum = 0
    while x > 0:
        digit = x % 10 
        sum = sum + digit * digit * digit
        x = x // 10
    return sum

x = 21
if armstrong(x):
        print("Yes, it is an Armstrong Number")
else:
        print("No, it is not an Armstrong Number")