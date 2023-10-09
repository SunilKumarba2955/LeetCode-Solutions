class Solution:
  def binarySearch(self, arr, x, findLeft):
    left, right = 0, len(arr)-1
    res = -1
    while left<=right:
      mid = (left+right)//2

      if arr[mid]==x:
        res = mid
        if findLeft:
          right = mid-1
        else:
          left = mid+1
      elif arr[mid]<x:
        left = mid+1
      else:
        right = mid-1
    return res

  def searchRange(self, nums: List[int], target: int) -> List[int]:
    return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]