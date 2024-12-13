class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        map = {}
        for c in chars:
            map[c] = map.get(c,0) + 1
        sum = 0
        for word in words:
            temp = {}
            isGood = True
            for c in word:
                temp[c] = temp.get(c,0) + 1
                if(temp[c] > map.get(c,0)):
                    isGood = False
                    break
            if isGood:
                sum += len(word)
        return sum


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        map = [0] * 26 
        for c in chars:
            map[ord(c)- ord('a')] += 1
     
        sum = 0
        for word in words:
            temp = [0] * 26
            isGood = True
            for c in word:
                temp[ord(c) - ord('a')] += 1
                if(temp[ord(c) - ord('a')] >  map[ord(c)- ord('a')] ):
                    isGood = False
                    break
            if isGood:
                sum += len(word)
        return sum