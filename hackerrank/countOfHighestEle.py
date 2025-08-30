#Solution 1 works but will get TLE
def birthdayCakeCandlesHashmap(candles):
    # Write your code here
    frequency = {}
    
    for i in candles:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1

    count = 0 
    for ele in frequency:
        if ele == max(frequency):
            count = frequency[ele]

    return count

print(birthdayCakeCandlesHashmap(candles=[4,4,1,3]))

def birthdayCakeCandlesWithoutHashmap(candles):
    max_height = -1
    count = 0

    for i in candles:
        if i > max_height:
            max_height = i
            count = 1
        elif i == max_height:
            count = count + 1

    return count


print(birthdayCakeCandlesWithoutHashmap(candles=[4,4,1,3]))


