class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res, stack = [0]*len(temp), []
        for i in range(len(temp)-1, -1, -1):
            while stack and temp[i]>=temp[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1]-i
            stack.append(i)
        return res