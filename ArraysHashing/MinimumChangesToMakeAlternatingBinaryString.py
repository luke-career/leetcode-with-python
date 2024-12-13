class Solution:
    def minOperations(self, s: str) -> int:

        model1 = ""
        for i in range(len(s)):
            if i % 2 == 0:
                model1 += "1"
            else:
                model1 += "0"
        model2 = ""
        for i in range(len(s)):
            if i % 2 == 0:
                model2 += "0"
            else:
                model2 += "1"

        return min(self.helper(s, model1), self.helper(s, model2))

    def helper(self, s1: str, s2: str) -> int:
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count


class Solution:
    def minOperations(self, s: str) -> int:
        model1 = ''
        model2 = ''
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            model1 =  '0' if i % 2 == 0 else '1'
            model2 =  '1' if i % 2 == 0 else '0'

            if(s[i] != model1):
                count1 += 1
            if(s[i] != model2):
                count2 += 1
            
        return min(count1,count2)
                