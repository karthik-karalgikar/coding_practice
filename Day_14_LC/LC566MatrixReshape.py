def matrixReshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])

    if m * n != r * c:
        return mat
    
    ans = []
    count = 0
    row = []
    
    for i in range(m):
        for j in range(n):
            row.append(mat[i][j])
            count = count + 1

            if count == c:
                ans.append(row)
                row = []
                count = 0

    return ans

mat = [[1, 2], [3, 4]]
r = 4
c = 1
result = matrixReshape(mat, r, c)
print(result)

'''
TRACING:

mat = [[1, 2], [3, 4]]
r = 1
c = 4

m = len(mat) -> 2
n = len(mat[0]) -> 2

m * n != r * c => 2 * 2 != 1 * 4 -> False

ans = []
row = []
count = 0

for i in range(m): 
    for j in range(n):
        => i = 0, j = 0
        row.append(mat[i][j]) -> row.append(mat[0][0])
        => row = [1]
        count = count + 1 => count = 1

        if count == c: -> count = 1, c = 4 -> false
        does not go inside

        => i = 0, j = 1
        row.append(mat[i][j]) -> row.append(mat[0][1])
        => row = [1, 2]
        count = count + 1 => count = 2

        if count == c: -> count = 2, c = 4 -> false
        does not go inside

        => i = 1, j = 0
        row.append(mat[i][j]) -> row.append(mat[1][0])
        => row = [1, 2, 3]
        count = count + 1 => count = 3

        if count == c: -> count = 3, c = 4 -> false
        does not go inside

        => i = 1, j = 1
        row.append(mat[i][j]) -> row.append(mat[1][1])
        => row = [1, 2, 3, 4]
        count = count + 1 => count = 4

        if count == c: -> count = 4, c =4 -> true
        goes inside

        ans.append(row) -> ans = [[1, 2, 3, 4]]
        row = []
        count = 0

        return ans
        ans = [[1, 2, 3, 4]]
'''