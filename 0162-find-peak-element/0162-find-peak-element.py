class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        low = 0
        high = n - 1
        
        while low < high:
            mid = low + ((high - low) >> 1)
            if nums[mid] >= nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low