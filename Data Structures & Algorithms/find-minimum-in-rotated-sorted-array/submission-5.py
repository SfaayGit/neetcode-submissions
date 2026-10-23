class Solution:
    def findMin(self, nums: List[int]) -> int:
        best = float('inf')
        left, right = 0, len(nums)-1 
        while left <= right:
            mid = (left+right) // 2
            soleft,sofar = 0,0
            if (nums[left] <= nums[mid]):
                soleft = nums[left]
                best = min(best, nums[left])
                left = mid + 1
            else:
                sofar = nums[mid]
                best = min(best, nums[mid])
                right = mid -1
        return best
