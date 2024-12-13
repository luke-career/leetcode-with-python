class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        des = ""
        mySet = set()
        for path in paths:
            mySet.add(path[0])
        for path in paths:
            if(path[1] not in mySet):
                des = path[1]    
        return des
        