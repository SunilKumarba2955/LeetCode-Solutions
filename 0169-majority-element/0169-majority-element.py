from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hsh = defaultdict(int)
        max = 0
        ele = 0
        for i in nums:
            hsh[i]+=1
            if max<hsh[i]:
                max = hsh[i]
                ele = i
            
            if max>len(nums):
                return ele
        
        return ele
        