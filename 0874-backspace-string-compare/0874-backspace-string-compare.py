class Solution:
    def solve(self, s):
        stack = []
        for i in s:
            if stack and i=='#':
                stack.pop()
            elif i!='#':
                stack.append(i)
        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.solve(s)
        t = self.solve(t)
        return s==t