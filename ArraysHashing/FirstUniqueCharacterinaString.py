class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        myMap = {}
        for char in s :
            myMap[char] = (myMap.get(char) or 0) + 1
        for i in range(len(s)):
            if myMap[s[i]] == 1:
                return i
                break
        return res

class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        myMap = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            myMap[index] += 1

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if(myMap[index] == 1):
                return i
        return res