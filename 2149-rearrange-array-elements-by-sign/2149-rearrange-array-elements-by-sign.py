class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range(len(nums)-1,-1,-2):
            nums[i-1] = pos.pop()
            nums[i] = neg.pop()
        return nums