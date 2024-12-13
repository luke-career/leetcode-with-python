class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums) / 3
        my_map = {}
        res = []
        for num in nums:
            my_map[num] = my_map.get(num,0) + 1
        
        for key,value in my_map.items():
            if(value > length):
                res.append(key)
        return res

        