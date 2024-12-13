class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        myMap = {}
        for word in words:
            for char in word:
                if char in myMap:
                    myMap[char] += 1
                else:
                    myMap[char] = 1
        
        res = list(myMap.values())
        for i in res:
            if i % len(words) != 0:
                return False
        return True


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        res = [0] * 26
        length = len(words)
        for item in words:
            for char in item:
                res[ord(char) - ord('a')] += 1

        for i in res:
            if i % length != 0:
                return False
        return True
