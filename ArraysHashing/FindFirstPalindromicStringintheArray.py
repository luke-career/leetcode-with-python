class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def helper(word:str) -> bool:
            l,r = 0,len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for word in words:
            if helper(word):
                return word
        return ""