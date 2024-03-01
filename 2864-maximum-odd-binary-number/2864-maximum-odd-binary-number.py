class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count('1')
        return (ones-1)*'1'+(n-ones)*'0'+'1'