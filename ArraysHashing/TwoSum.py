class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        my_dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in my_dic:
                return[my_dic.get(target - nums[i]),i]
            else:
                my_dic[nums[i]] = i

        return [] 