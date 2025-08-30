def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleDistance = []
    orangeDistance = []
    appleResult = []
    orangeResult = []
    for i in apples:
        appleDistance.append(i + a)
            
    for i in oranges: 
        orangeDistance.append(i + b)
            
    for i in appleDistance:
        if s <= i <= t:
            appleResult.append(i)
                
    for i in orangeDistance:
        if s <= i <= t:
            orangeResult.append(i)
                
    a = len(appleResult)
    b = len(orangeResult)

    print(a)
    print(b)

countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])