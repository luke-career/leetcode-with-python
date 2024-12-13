class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        mySet = set()
        for item in nums:
            if item in mySet:
                res.append(item)
            else:
                mySet.add(item) 

        for i in range(1,len(nums) + 1):
            if i not in mySet:
                res.append(i)

        return res

        