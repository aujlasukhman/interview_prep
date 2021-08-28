def isValidSudoku(board) -> bool:
    isValid = True
    
    def validnumbers(numbers):
        flagarray = [0]*9
        for number in numbers:
            if number.isdigit():
                number = int(number)
                if flagarray[number-1] == 0:
                    flagarray[number-1] = 1
                else:
                    flagarray[number-1] = -1
                    return False
        return True
        
    def column(colnum):
        col = []
        for i in range(9):
            col.append(board[i][colnum])
            
        return col
    
    def box(row,col):
        box_numbers = []
        for i in range(row,row+3):
            for j in range(col,col+3):
                box_numbers.append(board[i][j])
        return box_numbers
                
    
    #print(board[0][1].isdigit())
    for row in board:
        isValid = isValid and validnumbers(row)
    
    for colnum in range(9):
        isValid = isValid and validnumbers(column(colnum))
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            isValid = isValid and validnumbers(box(i,j))

    return isValid

print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))