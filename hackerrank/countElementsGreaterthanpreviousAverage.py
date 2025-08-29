def countResponseTimeRegressions(responseTimes):
    # Write your code here
    count = 0
    for i in range(len(responseTimes)):
        if i == 0:
            continue
        if responseTimes[i] > sum(responseTimes[:i])/i:
            count = count + 1
    
    return count

print(countResponseTimeRegressions(responseTimes=[100, 200, 150, 300]))

'''
TRACING :

responseTimes = [100, 200, 150, 300]
count = 0

for i in range(len(responseTimes)):
    -> i = 0
    if i == 0:
        continue
        
    -> i = 1
    if responseTimes[i] > sum(responseTimes[:i]) / i:
    -> responseTimes[1] > sum(responseTimes[:1]) / 1
    -> 200 > sum(100) / 1
    -> 200 > 100 -> true
        count = count + 1
        count = 1

    -> i = 2
    if responseTimes[i] > sum(responseTimes[:i]) / i:
    -> responseTimes[2] > sum(responseTimes[:2]) / 2
    -> 150 > sum(100 + 200) / 2
    -> 150 > 150 => false, does not go inside if statement

    i = 3
    if responseTimes[i] > sum(responseTimes[:i]) / i:
    -> responseTimes[3] > sum(responseTimes[:3]) / 3
    -> 300 > sum(100 + 200 + 150) / 3
    -> 300 > 150 -> true
        count = count + 1
        count = 2

    i = 4 -> out of range

Output -> count = 2
'''