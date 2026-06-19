class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in  range(9):
            h=[]
            for j in range (9):
                if ord(board[i][j])>48:
                    if board[i][j] in h:
                        return False
                    else:
                        h.append(board[i][j])
        
        for i in  range(9):
            h=[]
            for j in range (9):
                if ord(board[j][i])>48:
                    if board[j][i] in h:
                        return False
                    else:
                        h.append(board[j][i])     
        h1=[]
        h2=[]
        h3=[]
        h4=[]
        h5=[]
        h6=[]
        h7=[]
        h8=[]
        h9=[]
        for i in range (9):
            
            for j in range (9):
                if i < 3 and j<3:
                    if ord(board[i][j])>48:
                        if board[i][j] in h1:
                            return False
                        else:
                            h1.append(board[i][j])
                if 3 <= i < 6 and j<3:
                    if ord(board[i][j])>48:
                        if board[i][j] in h2:
                            return False
                        else:
                            h2.append(board[i][j])
                if 6 <= i and j<3:
                    if ord(board[i][j])>48:
                        if board[i][j] in h3:
                            return False
                        else:
                            h3.append(board[i][j])
                if 3 <= j < 6 and i<3:
                    if ord(board[i][j])>48:
                        if board[i][j] in h4:
                            return False
                        else:
                            h4.append(board[i][j])
                if 3 <= i < 6 and 3 <= j < 6 :
                    if ord(board[i][j])>48:
                        if board[i][j] in h5:
                            return False
                        else:
                            h5.append(board[i][j])
                if i >= 6 and 3 <= j < 6:
                    if ord(board[i][j])>48:
                        if board[i][j] in h6:
                            return False
                        else:
                            h6.append(board[i][j])
                if 3 > i and j>=6:
                    if ord(board[i][j])>48:
                        if board[i][j] in h7:
                            return False
                        else:
                            h7.append(board[i][j])
                if 3 <= i < 6 and j>=6:
                    if ord(board[i][j])>48:
                        if board[i][j] in h8:
                            return False
                        else:
                            h8.append(board[i][j])
                if i >= 6 and j>=6:
                    if ord(board[i][j])>48:
                        if board[i][j] in h9:
                            return False
                        else:
                            h9.append(board[i][j])
        return True
