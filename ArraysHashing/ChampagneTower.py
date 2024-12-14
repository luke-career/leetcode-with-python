class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
     
        arr = [[0.0] * (i + 1) for i in range(query_row + 1)]
       # row,col = query_row + 1,query_glass + 1 
       # arr = [[0 for _ in range(col)] for _ in range(row)]
        arr[0][0] = poured
        for i in range(len(arr) - 1):
            for j in range(i + 1):
                if(arr[i][j] > 1):
                    arr[i +1][j] += (arr[i][j] - 1) / 2
                    arr[i+ 1][j+1] += (arr[i][j] - 1) / 2
                    arr[i][j] = 1
        
        return min(1,arr[query_row][query_glass])
           