#Solution 1

num = input()
arm=0
for i in num:
    arm = arm + pow(int(i),len(num))
print(arm)
if arm!=int(num):
    print(False)
else:
    print(True)

'''
TRACING 

num = 153
for loop:
    i = 1
    arm = 0 +pow(1, 3) -> 0 + 1^3 -> 1
    i = 5
    arm = 1 + pow(5, 3) -> 1 + 5^3 -> 126
    i = 3
    arm = 126 + pow(3, 3) -> 126 + 3^3 -> 153
out of the for loop

'''

#Solution 2

def armstrong(num):
    arm = 0
    n=len(str(num))
    while num > 0:
        temp = num % 10
        num = num // 10
        arm = arm + temp**n
    return arm

num = int(input())
dummy = num
result = armstrong(num)
if dummy == result:
    print(True)
else:
    print(False)

'''
TRACING
num = 153 
n = len(153) -> 3

temp = 153 % 10 -> 3
num = 153 // 10 -> 15
arm = 0 + 3**3 -> 27

temp = 15 % 10 -> 5
num = 15 // 10 -> 1
arm = 27 + 5**3 -> 152

temp = 1 % 10 -> 1
num = 1 // 10 -> 0
arm = 152 + 1**3 -> 153

'''