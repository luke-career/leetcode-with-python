class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = 0
        for item in nums:
            if count == 0:
                majority = item
            if majority == item:
                count += 1
            else:
                count -= 1
        return majority


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myMap = {}
        for item in nums:
            myMap[item] = myMap.get(item,0) + 1
        

        return max(myMap,key = myMap.get)
