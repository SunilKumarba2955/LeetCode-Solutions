class Solution:
    def eval(self, op1, op, op2):
        if op=='+':
            return op1+op2
        if op=='-':
            return op1-op2
        if op=='*':
            return op1*op2
        if op=='/':
            return int(op1/op2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ('+', '*', '-', '/'):
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.eval(op1, i, op2))
            else:
                stack.append(int(i))
        return stack.pop()