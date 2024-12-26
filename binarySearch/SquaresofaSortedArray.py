class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums) - 1
        index = r
        res = [0] * len(nums)
        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            if left > right:
                res[index] = left
                l += 1
            else:
                res[index] = right
                r -= 1
            index -= 1
        return res
            
        