def longestpath(matrix,r,c):
    if len(matrix) == 0:
        return None
    if len(matrix) == 1:
        return 1
    table = {}
    
    maxLen = 0
    def dfs(x,y,table,prev):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] >= prev:
            return 0

        if (x,y) in table:
            return table[(x,y)]

        path = 1 + max(dfs(x-1,y,table,matrix[x][y]),dfs(x+1,y,table,matrix[x][y]),dfs(x,y-1,table,matrix[x][y]),dfs(x,y+1,table,matrix[x][y]))
        table[(x,y)] = path
        nonlocal maxLen
        maxLen = max(maxLen,path)

        return path
    
    dfs(r,c,table,1000)
    print(table)
    return maxLen

print(longestpath([[9,9,4],[6,6,8],[2,1,1]],0,0))