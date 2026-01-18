def maxProfit(prices):
    k = 0
    result = 0
    prices.append(-1)

    if prices[0] <= prices[1]:
        k = prices[0]

    for i in range(1, len(prices) - 1):
        if prices[i] < prices[i - 1]:
            k = prices[i]
        elif prices[i] > prices[i + 1]:
            result = result + prices[i] - k

    return result

print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))

'''
TRACING - 
prices = [7, 1, 5, 3, 6, 4]

k = 0
result = 0
prices.append(-1)
=> prices = [7, 1, 5, 3, 6, 4, -1]

if prices[0] <= prices[1]:
7 <= 1 -> false

for i in range(1, len(prices) - 1):
    -> i = 1
    if prices[1] < prices[i - 1]:
    1 < 7 -> true
        k = prices[i]
        k = 1
    
    -> i = 2
    if prices[2] < prices[1]:
    5 < 1 -> false

    elif prices[i] > prices[i + 1]:
    5 > 3 -> true
        result = result + prices[i] - k
        result = 0 + 5 - 1
        result = 4

    -> i = 3
    if prices[3] < prices[2]:
    3 < 5 -> true
        k = prices[i] 
        k = 3

    -> i = 4
    if prices[i] < prices[i - 1]:
    6 < 3 -> false

    elif prices[i] > prices[i + 1]:
    6 > 4 -> true
        result = result + prices[i] - k
        result = 4 + 6 - 3
        result = 7

    -> i = 5
    if prices[i] < prices[i - 1]:
    4 < 6 -> true
        k = prices[i] 
        k = 4

return result 

result = 7
    
'''