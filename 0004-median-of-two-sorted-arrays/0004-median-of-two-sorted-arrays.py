class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def swapIfGreater(a,b,i,j):
            if a[i]>b[j]:
                a[i],b[j] = b[j],a[i]
                
        n,m = len(nums1), len(nums2)
        size = n+m
        if n==0 and m==0:
            return 0
        if n==0:
            return nums2[size//2] if size%2!=0 and size!=1 else (nums2[size//2]+nums2[size//2-1])/2
        if m==0:
            return nums1[size//2] if size%2!=0 and size!=1 else (nums1[size//2]+nums1[size//2-1])/2

        gap = size//2+size%2
        while gap>0:
            left, right = 0, gap
            while right<size:
                if left<n and right>=n:
                    swapIfGreater(nums1, nums2, left, right-n)
                elif left>=n:
                    swapIfGreater(nums2, nums2, left-n, right-n)
                else:
                    swapIfGreater(nums1, nums1, left, right)
                left+=1
                right+=1
            if gap==1:
                break
            gap = gap//2+gap%2
        nums1=nums1+nums2
        return (nums1[size//2]+nums1[size//2-1])/2 if size%2==0 else nums1[size//2]
