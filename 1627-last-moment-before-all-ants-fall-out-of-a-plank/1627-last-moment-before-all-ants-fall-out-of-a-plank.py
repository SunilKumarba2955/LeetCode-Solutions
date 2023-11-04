class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        time = 0
        if left:
            time = max(left)
        for pos in right:
            time = max(time, n - pos)
        return time