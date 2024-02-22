class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        L = [[1]]
        for i in range(numRows-1):
            L.append([1])
            j = 0
            while j<len(L[i])-1 and len(L[i])>1:
                L[i+1].append(L[i][j] + L[i][j+1])
                j+=1
            L[i+1].append(1)
        return L
        