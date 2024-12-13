class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1,9):
            n = i
            for j in range(i + 1,10):
                n = n * 10 + j
                if n >= low and n <= high:
                    res.append(n)
                elif n > high:
                    break
        return sorted(res)
                