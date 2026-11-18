class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != '.':
                    if int(board[i][j]) < 1 or int(board[i][j]) > 9 or int(board[i][j]) in s:
                        return False
                    s.add(int(board[i][j]))
            s = set()
            for j in range(9):
                if board[j][i] != '.':
                    if int(board[j][i]) < 1 or int(board[j][i]) > 9 or int(board[j][i]) in s:
                        return False
                    s.add(int(board[j][i]))
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] != '.':
                            if int(board[k][l]) < 1 or int(board[k][l]) > 9 or int(board[k][l]) in s:
                                return False
                            s.add(int(board[k][l]))
        return True