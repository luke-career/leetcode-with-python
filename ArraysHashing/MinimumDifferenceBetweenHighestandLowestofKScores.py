class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minNumber = float('inf')
        for i in range(len(nums) - k + 1):
            minNumber = min(minNumber,nums[i + k - 1] - nums[i])
        return minNumber


        