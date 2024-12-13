class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0] * len(nums) 
        rightSum = [0] * len(nums)
        sum = 0
        for i in range(len(nums)):
            leftSum[i] = sum
            sum += nums[i]
        sum = 0
        for i in range(len(nums) - 1, -1,-1):
            rightSum[i] = sum
            sum += nums[i]
        
        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i

        return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = 0
        totalSum = sum(nums)
        for i in range(len(nums)):
            if(totalSum - leftSum - nums[i] == leftSum):
                return i
            leftSum += nums[i]
        return -1
        