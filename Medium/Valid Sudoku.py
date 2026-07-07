class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        rows=collections.defaultdict(list)
        cols=collections.defaultdict(list)
        sq=collections.defaultdict(list)
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j]==".":
                    continue
                
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sq[(i//3,j//3)]:
                    return False
                
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                sq[(i//3,j//3)].append(board[i][j])
                
                
        return True