class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]

        for i in range(rowIndex + 1):
            current = [1]
            for j in range(1,i + 1):
                if j == 0 or j == i:
                    current.append(1)
                else: 
                    current.append(pre[j] + pre[j - 1])
            pre = current
        return pre
        