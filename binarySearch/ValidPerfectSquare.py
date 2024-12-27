class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0,num
        while l <= r:
            mid = l + (r - l) // 2
            res = mid * mid
            if res > num:
                r = mid - 1
            elif res < num:
                l = mid + 1
            else:
                return True
        return False
        