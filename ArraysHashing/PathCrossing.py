class Solution:
    def isPathCrossing(self, path: str) -> bool:
        p = [0,0]
        start = str(p[0]) + ',' + str(p[1])
        res = set()
        res.add(start)
        for s in path:
            if s == 'N':
                p[1] += 1
            elif s == 'S':
                p[1] -= 1
            elif s == 'E':
                p[0] += 1
            elif s == 'W':
                p[0] -= 1
            route = str(p[0]) + ',' + str(p[1])
            if route in res:
                return True
            else:
                res.add(route)
        return False 
        