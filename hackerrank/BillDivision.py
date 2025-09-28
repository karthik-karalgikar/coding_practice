def bonAppetit(bill, k, b):
    # Write your code here
    ootaSum = sum(bill[0:k] + bill[k + 1 :])
    AnnaShare = ootaSum // 2
    
    if AnnaShare == b:
        print('Bon Appetit')
    else:
        print(b - AnnaShare)

bonAppetit([3, 10, 2, 9], 1, 7)

'''
TRACING - 
bill = [3, 10, 2, 9]
k = 1 (portion of oota Anna did not eat)
b = 7 (total amount of money chared for Anna)

since k is the portion of food anna did not eat, we have to skip that. 

so, 
ootaSum = sum(bill[0 : k] + bill[k + 1: ])
ootaSum = sum(bill[0 : 1] + bill[2 : 4])
ootaSum = sum(bill[0] + bill[2] + bill[3])
ootaSum = sum(3 + 2 + 9)
ootaSum = 14

AnnaShare = ootaSum // 2 -> 14 // 2 
AnnaShare = 7

if AnnaShare == b:
7 == 7 -> true
    print('Bon Appetit')

Output = Bon Appetit

if it was 12, 
if Annashare == b:
7 == 12 -> false

else:
    print(b - AnnaShare)
    print(12 - 7)

Output = 5
'''