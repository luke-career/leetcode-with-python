class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = 0
        myMap = {}
        maxLength = 0
        myMap[0] = -1

        for i in range(len(nums)):
            temp = -1 if nums[i] == 0 else 1
            pre += temp
            if pre in myMap:
                maxLength = max(maxLength,i - myMap[pre])
            else: 
                myMap[pre] = i
        return maxLength
                
