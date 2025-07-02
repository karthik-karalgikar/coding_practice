#same as 2016, but will get TLE with the same code, so have to use sliding window. 

def maxProfit(prices):
    max_diff = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if i < j and prices[i] < prices[j]:
                diff = prices[j] - prices[i]
                max_diff = max(max_diff, diff)

    if max_diff == 0:
        return 0
    
    return max_diff

print(maxProfit(prices = [7,1,5,3,6,4]))

#Sliding window

def maxProfitSlidingWindow(prices):
    min_price = float('inf')
    max_profit = 0

    for i in prices:
        if i < min_price:
            min_price = i
        else:
            profit = i - min_price
            max_profit = max(max_profit, profit)

    return max_profit

print(maxProfitSlidingWindow(prices = [7,1,5,3,6,4]))

'''
TRACING :

min_price = inf
max_profit = 0

for i in prices:
    -> i = 7
    if i < min_price: -> 7 < inf => true
        min_price = i
        mind_price = 7

    -> i = 1
    if i < min_price: -> 1 < 7 -> true
        min_price = i
        min_price = 1

    -> i = 5
    if i < min_price: -> 5 < 1 -> false
    else:
        profit = i - min_price -> 5 - 1
        profit = 4
        max_profit = max(profit, max_profit)
        max_profit = max(4, 0)
        max_profit = 4

    -> i = 3
    if i < min_price: -> 3 < 1 -> false
    else:
        profit = i - min_price -> 3 - 1
        profit = 2
        max_profit = max(profit, max_profit)
        max_profit = max(2, 4)
        max_profit = 4

    -> i = 6
    if i < min_price: -> 6 < 1 -> false
    else:
        profit = i - min_price -> 6 - 1
        profit = 5
        max_profit = max(profit, max_profit)
        max_profit = max(5, 4)
        max_profit = 5

    -> i = 4
    if i < min_price: -> 4 < 1 -> false
    else:
        profit = i - min_price -> 4 - 1
        profit = 3
        max_profit = max(profit, max_profit)
        max_profit = max(3, 5)
        max_profit = 5

    exits loop

    return max_profit

    Output = 5
'''
