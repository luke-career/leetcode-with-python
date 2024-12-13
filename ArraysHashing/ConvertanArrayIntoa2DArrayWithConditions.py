class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        s = Counter(nums)
        res = []
        while True:
            temp = []
            for key,value in s.items():
                if value > 0:
                    temp.append(key)
                    s[key] = value - 1
            if len(temp) == 0:
                break
            res.append(temp)
        return res
            

