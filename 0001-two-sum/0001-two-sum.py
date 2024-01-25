class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in numMap:
                return [numMap[c], i]
            numMap[nums[i]] = i
        return []
