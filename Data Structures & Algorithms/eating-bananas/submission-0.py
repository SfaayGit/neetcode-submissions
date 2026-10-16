class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1, max(piles)
        best = right
        while left <= right:
            mid = (left+right) //2
            sum = 0
            for i in piles:
                sum = sum + math.ceil(i/mid)
            if (sum > h):
                left = mid+1
            else:
                right = mid-1
                best = mid
        return best