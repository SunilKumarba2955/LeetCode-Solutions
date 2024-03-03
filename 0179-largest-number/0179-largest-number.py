class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            x = str(x)
            y = str(y)
            xy=x+y
            yx=y+x
            if xy<yx:
                return 1
            elif xy>yx:
                return -1
            else:
                return 0
        a=""
        nums.sort(key=cmp_to_key(compare))
        for i in range(len(nums)):
            a+=str(nums[i])
        return "0" if a[0] == "0" else a