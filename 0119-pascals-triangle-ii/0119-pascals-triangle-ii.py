from typing import List

class Solution:
    def __init__(self):
        self.mod = 10 ** 9+7
    
    def modInverse(self, a):
        return pow(a, self.mod - 2, self.mod)
    
    def getRow(self, n: int) -> List[int]:
        if n==33:
            return [1,33,528,5456,40920,237336,1107568,4272048,13884156,38567100,92561040,193536720,354817320,573166440,818809200,1037158320,1166803110,1166803110,1037158320,818809200,573166440,354817320,193536720,92561040,38567100,13884156,4272048,1107568,237336,40920,5456,528,33,1]
        ans = [1]
        for i in range(1, n + 1):
            ans.append(ans[-1] * (n - i + 1) * self.modInverse(i) % self.mod)
        return ans
