class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        max = nums[len(nums) - 1] * nums[len(nums) - 2]
        min = nums[0] * nums[1]
        return max - min