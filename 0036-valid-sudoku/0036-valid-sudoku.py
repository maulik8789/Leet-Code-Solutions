class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ans=[]
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x!='.':
                    ans+=[(i,x),(x,j),(i//3,j//3,x)]
        return len(ans)==len(set(ans))
        
        # Runtime: 87 ms, faster than 85.09% of Python3 online submissions for Valid Sudoku.
        # res=[]
        # for i in range(9):
        #     for j in range(9):
        #         ele = board[i][j]
        #         if ele!='.':
        #             res+=[(i,ele),(ele,j),(i//3,j//3,ele)]
        # return len(res)==len(set(res))