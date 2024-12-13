class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxNumber = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                maxNumber = max(maxNumber, int(num[i : i +3]))
        
        if maxNumber == 0:
            return "000"
        elif maxNumber == -1:
            return ""
        else:
            return str(maxNumber)

        