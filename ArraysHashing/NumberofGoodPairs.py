class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        map = {}
        for num in nums:
            if num in map:
                temp = map[num]
                count += temp
                map[num] = temp + 1
            else:
                map[num] = 1
        return count