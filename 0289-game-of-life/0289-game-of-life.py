class Solution:
    def check(self, b, i,j,m,n):
        if i>=0 and i<m and j>=0 and j<n and b[i][j]==1:
            return 1
        return 0
    def count(self, b, i,j,m,n):
        c = 0
        c+=self.check(b,i-1, j-1, m,n)
        c+=self.check(b,i-1, j, m,n)
        c+=self.check(b,i-1, j+1, m,n)
        c+=self.check(b,i, j-1, m,n)
        c+=self.check(b,i, j+1, m,n)
        c+=self.check(b,i+1, j-1, m,n)
        c+=self.check(b,i+1, j, m,n)
        c+=self.check(b,i+1, j+1, m,n)
        return c

            
    def gameOfLife(self, board: List[List[int]]) -> None:
        dummy =deepcopy(board)
        m,n = len(board), len(board[0])
        new = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                res = self.count(dummy,i,j,m,n)
                # print(i, j, res)
                if dummy[i][j]==1:
                    if res<2: board[i][j]=0
                    if res==2 or res==3: board[i][j]=1
                    if res>3: board[i][j]=0
                else:
                    if res==3: board[i][j]=1
        return board