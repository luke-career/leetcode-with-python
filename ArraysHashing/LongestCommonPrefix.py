class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return " "
        min_str = min(strs,key = len)
        min_length = len(min_str)

        j = 0
        while j < min_length:
            for i in range(1,len(strs)):
              if strs[i][j] != strs[0][j]:
                return strs[0][0:j]
            j += 1
        return strs[0][0:j]