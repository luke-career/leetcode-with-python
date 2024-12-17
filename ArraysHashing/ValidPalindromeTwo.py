class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s_reverse:str) -> bool:
            return s_reverse == s_reverse[::-1]

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            l += 1
            r -= 1
        
        return True