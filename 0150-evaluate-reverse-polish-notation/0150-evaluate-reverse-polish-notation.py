class Solution:
    def eval(self, op2, op, op1):
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
        op = set(['+', '-', '*', '/'])
        for i in tokens: stack.append(self.eval(stack.pop(), i, stack.pop()) if i in op else int(i))
        return stack.pop()