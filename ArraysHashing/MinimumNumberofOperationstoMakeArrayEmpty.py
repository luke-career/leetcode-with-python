class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        my_map = {}
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i],0) + 1
        

        for value in my_map.values():
            if value == 1:
                return -1
            
            count += value // 3

            if value % 3 != 0:
                count += 1

        return count

        