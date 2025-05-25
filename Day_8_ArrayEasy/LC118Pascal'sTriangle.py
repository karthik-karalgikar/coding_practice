def generate(self, numRows):
    List=[]
    list_0=[1]
    list_1=[1,1]
    List.append(list_0)
    List.append(list_1)
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]
    if numRows>=3:
        for i in range(2,numRows):
            list_i=[1]
            for j in range (1,i):
                list_i.append(List[i-1][j-1]+List[i-1][j])
            list_i.append(1)
            List.append(list_i)
    return List