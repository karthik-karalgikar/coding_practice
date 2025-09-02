def generate(numRows):
    endList=[]
    list_0=[1]
    list_1=[1,1]
    endList.append(list_0)
    endList.append(list_1)
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1, 1]]
    if numRows>=3:
        for i in range(2,numRows):
            list_i=[1]
            for j in range (1,i):
                list_i.append(endList[i - 1][j - 1]+endList[i - 1][j])
            list_i.append(1)
            endList.append(list_i)
    return endList


print(generate(numRows=5))

'''
TRACING :

numRows = 5

endList = []
list_0 = [1]
list_1 = [1, 1]

endList.append(list_0)
=> endList = [[1]]

endList.append(list_1)
=> endlist = [[1], [1, 1]]

if numRows == 1:
    -> false

if numRows == 2:
    -> false

else:
    for i in range(2, numRows):
        -> i = 2
        list_i = [1]
        => list_2 = [1]
        for j in range(1, i):
            -> j = 1, until i = 2 (basically only one loop here)

            list_i.append(endList[i - 1][j - 1] + endlist[i - 1][j])
            NOTE => endList = [[1], [1, 1]]
            => list_2.append(endList[2 - 1][1 - 1] + endList[2 - 1][1])
            => list_2.append(endList[1][0] + endList[1][1])
            => list_2.append(1 + 1)
            => list_2.append(2)
            list_2 = [1, 2]

            -> j = 2 -> out of range

        list_i.append(1)
        list_2.append(1)
        list_2 = [1, 2, 1]

        endList.append(list_i)
        endList = [[1], [1, 1], [1, 2, 1]]

        -> i = 3
        list_i = [1]
        => list_3 = [1]

        for j in range(1, i):
            -> j = 1, i = 3

            list_i.append(endList[i - 1][j - 1] + endList[i - 1][j])
            list_3.append(endList[2][0] + endList[2][1])
            NOTE : endList = [[1], [1, 1], [1, 2, 1]]
            list_3.append(1 + 2)
            list_3 = [1, 3]

            -> j = 2, i = 3

            list_i.append(endList[i - 1][j - 1] + endList[i - 1][j])
            list_3.append(endList[2][1] + endList[2][2])
            NOTE : endList = [[1], [1, 1], [1, 2, 1]]
            list_3.append(2 + 1)
            list_3 = [1, 3, 3]

            -> j = 3, i = 3 -> out of range

        list_i.append(1)
        list_3.append(1)
        list_3 = [1, 3, 3, 1]

        endList.append(list_i)
        endList.append(list_3)

        endList = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

        -> i = 4
        list_i = [1]
        list_4 = [1]

        for j in range(1, i):
            -> j = 1, i = 4
            list_i.append(endList[i - 1][j - 1] + endList[i - 1][j])
            NOTE : endList = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
            list_4.append(endList[3][0] + endList[3][1])
            list_4.append(1 + 3)
            list_4 = [1, 4]

            -> j = 2, i = 4
            list_i.append(endList[i - 1][j - 1] + endList[i - 1][j])
            list_4.append(endList[3][1] + endList[3][2])
            list_4.append(3 + 3)
            list_4 = [1, 4, 6]

            -> j = 3, i = 4
            list_i.append(endList[i - 1][j - 1] + endList[i - 1][j])
            list_4.append(endList[3][2] + endList[3][3])
            list_4.append(3 + 1)
            list_4 = [1, 4, 6, 4]

            -> j = 4, j = 4 -> out of range

        list_i.append(1)
        list_4.append(1)
        list_4 = [1, 4, 6, 4, 1]

        endList.append(list_4)

        endList = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
                    
'''
