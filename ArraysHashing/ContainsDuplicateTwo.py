class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mySet = set()
        for i in range(len(nums)):
            if(nums[i] in mySet):
                return True
            mySet.add(nums[i])
            if(len(mySet) > k):
                mySet.remove(nums[i - k])
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}
        for i in range(len(nums)):
            if nums[i] in myMap:
                if i - myMap.get(nums[i]) <= k:
                    return True
            myMap[nums[i]] = i

        return False
    