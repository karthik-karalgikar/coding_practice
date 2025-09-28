def breakingRecords(scores):
    # Write your code here
    minScore = scores[0]
    maxScore = scores[0]
    
    maxResult = []
    minResult = []
    for i in range(1, len(scores)):
        if scores[i] > maxScore:
            maxScore = scores[i]
            maxResult.append(maxScore)
        elif scores[i] < minScore:
            minScore = scores[i]
            minResult.append(minScore)
        else:
            continue
            
    return len(maxResult), len(minResult)

print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))

'''
TRACING - 

minScore = scores[0]
minScore = 10

maxScore = scores[0]
maxScore = 10

maxResult = []
minResult = []

for i in range(1, len(scores)):
    i = 1
    if scores[i] > maxScore:
    scores[1] > maxScore -> 5 > 10 -> false

    elif scores[i] < minScore:
    scores[i] < minScore -> 5 < 10 -> true
        minScore = scores[i]
        minScore = 5
        minResult.append(minScore)

        minResult = [5]

    i = 2
    if scores[i] > maxScore:
    scores[2] > maxScore -> 20 > 10 -> true
        maxScore = scores[i]
        maxScore = 10
        maxResult.append(maxScore)

        maxResult = [20]

    i = 3
    if scores[i] > maxScore:
    scores[3] > maxScore -> 20 > 20 -> false

    elif scores[i] < minScore:
    scores[3] < minScore -> 20 < 5 -> false

    else:
        continue
        
    i = 4
    if scores[i] > maxScore:
    scores[4] > maxScore -> 4 > 20 -> false

    elif scores[i] < minScore:
    scores[4] < minScore -> 4 < 5 -> true
        minScore = scores[i]
        miScore = 4
        minResult.append(minScore)

        minResult = [5, 4]

    i = 5
    if scores[i] > maxScore:
    scores[5] > maxScore -> 5 > 20 -> false

    elif scores[i] < minScore:
    scores[5] < minScore -> 5 < 4 -> false

    else:
        continue
        
    i = 6
    if scores[i] > maxScore:
    scores[6] > maxScore -> 2 > 20 -> false

    elif scores[i] < minScore:
    scores[6] < minScore -> 2 < 4 -> true
    minScore = scores[i]
        minScore = 2
        minResult.append(minScore)

        minResult = [5, 4, 2]

    i = 7
    if scores[i] > maxScore:
    scores[7] > maxScore -> 25 > 20 -> true
    maxScore = scores[i]
        maxScore = 25
        maxResult.append(maxScore)

        maxResult = [20, 25]

    i = 8
    if scores[i] > maxScore:
    scores[8] > maxScore -> 1 > 25 -> false

    elif scores[i] < minScore:
    scores[8] < minScore -> 1 < 2 -> true
    minScore = scores[i]
        miScore = 1
        minResult.append(minScore)

        minResult = [5, 4, 2, 1]

    
return len(minScore), len(maxScore)

output = 2, 4
'''