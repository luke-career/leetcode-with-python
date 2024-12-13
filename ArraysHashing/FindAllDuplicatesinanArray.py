class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            p = abs(nums[i])
            if nums[p - 1] < 0:
                res.append(p)
            else:
                nums[p - 1] = - nums[p - 1]
        return res  

        