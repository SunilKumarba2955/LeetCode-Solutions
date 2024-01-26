class Solution:
    def helper(self, ch):
        match ch:
            case '2':
                return 'abc'
            case '3':
                return 'def'
            case '4':
                return 'ghi'
            case '5':
                return 'jkl'
            case '6':
                return 'mno'
            case '7':
                return 'pqrs'
            case '8':
                return 'tuv'
            case '9':
                return 'wxyz'
            case _:
                return ''

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        for ch in digits:
            s = self.helper(ch)
            if not res:
                res = [ i for i in s ]
            else:
                n = len(res)
                temp = []
                for i in range(n):
                    for j in s:
                        temp.append(res[i]+j)
                res = temp
        return res