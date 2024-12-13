class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxSize = -1
        myMap = {}
        for i in range(len(s)):
            char = s[i]
            if char in myMap:
                maxSize = max(i - myMap[char] - 1, maxSize)
            else:
                myMap[char] = i
        return maxSize        
        