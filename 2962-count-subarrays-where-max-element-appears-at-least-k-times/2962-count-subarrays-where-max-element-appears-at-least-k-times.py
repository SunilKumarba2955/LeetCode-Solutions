class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxnum = max(nums)
        ans = 0
        n = len(nums)

        maxind = [-1]  # Initialize with -1 to handle edge case
        for i in range(n):
            if nums[i] == maxnum:
                maxind.append(i)

        indsize = len(maxind)

        for i in range(1, indsize - k + 1):
            l = maxind[i] - maxind[i - 1] - 1
            r = n - 1 - maxind[i + k - 1]
            ans += (l + 1) * (r + 1)

        return ans