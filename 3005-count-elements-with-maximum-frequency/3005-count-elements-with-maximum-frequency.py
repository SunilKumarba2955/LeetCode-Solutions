from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        v = list(dic.values())
        mx = max(v)
        return v.count(mx)*mx