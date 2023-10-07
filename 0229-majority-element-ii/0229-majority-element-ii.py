class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = Counter(nums)
        ans = []
        for i,j in res.items():
            if j>(len(nums)//3):
                ans.append(i)
        return ans