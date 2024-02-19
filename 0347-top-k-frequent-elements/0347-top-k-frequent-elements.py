from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter = sorted(counter.items(), key=lambda x: x[1])
        keys = [counter[i][0] for i in range(len(counter)-1, len(counter)-k-1, -1)]
        return keys