class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(temp)==0 or len(temp)<=i+j:
                    temp.append([mat[i][j]])
                else:
                    temp[i+j].append(mat[i][j])
        res = []
        for i in range(len(temp)):
            if i%2==0:
                res.extend(temp[i][::-1])
            else:
                res.extend(temp[i])
        return res