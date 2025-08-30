#stupid solution: 
def gradingStudents(grades):
    result = []
    for i in range(len(grades)):
        if grades[i] < 38:
            result.append(grades[i])
        else:
            if (grades[i] + 1) % 5 == 0: 
                if (grades[i] + 1) - grades[i] < 3:
                    grades[i] = grades[i] + 1
                result.append(grades[i])
            elif (grades[i] + 2) % 5 == 0:
                if (grades[i] + 2) - grades[i] < 3:
                    grades[i] = grades[i] + 2
                result.append(grades[i])
            elif (grades[i] + 3) % 5 == 0:
                if (grades[i] + 3) - grades[i] < 3:
                    grades[i] = grades[i] + 3
                result.append(grades[i])
            elif (grades[i] + 4) % 5 == 0:
                if (grades[i] + 4) - grades[i] < 3:
                    grades[i] = grades[i] + 4
                result.append(grades[i])
                    
    return result

#good solution:
def grading(grades):
    result = []
    for g in grades:
        if g < 38:
            result.append(g)
        else:
            next_multiple = ((g // 5) + 1) * 5
            if next_multiple - g < 3:
                result.append(next_multiple)
            else:
                result.append(g)

    return result

print(grading(grades=[73, 62, 90, 23]))

'''
TRACING - 

result = [73, 62, 90, 23]

for g in grades:
    -> g = 73
    else:
        next_multiple = ((g // 5) + 1) * 5
        next_multiple = ((73 // 5) + 1) * 5 -> (14 + 1) * 5 -> 15 * 5 
        next_multiple = 75

        if next_multiple - g < 3:
        75 - 73 = 2 < 3 -> true
            result.append(next_multiple)

        result = [75]

    -> g = 62
    else:
        next_multiple = ((g // 5) + 1) * 5
        next_multiple = ((62 // 5) + 1) * 5 -> (12 + 1) * 5 -> 13 * 5
        next_multiple = 65

        if next_multiple - g < 3:
        65 - 62 = 3 < 3 -> false
        else:
            result.append(g)

        result = [75, 62]

    -> g = 90
    else:
        next_multiple = ((g // 5) + 1) * 5
        next_multiple = ((90 // 5) + 1) * 5 -> (18 + 1) * 5 -> 19 * 5
        next_multiple = 90

        if next_multiple - g < 3:
        95 - 90 = 5 < 3 -> false

        else:
            result.append(g)

        result = [75, 62, 90]

    -> g = 23
    if g < 38: -> true
        result.append(g)

    result = [75, 62, 90, 23]
'''
            