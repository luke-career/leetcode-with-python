class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        pre = []
        for i in range(numRows):
            current = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    current[j] = 1
                else:
                    current[j] = pre[j] + pre[j - 1]
                
            pre = current
            res.append(current)
        return res