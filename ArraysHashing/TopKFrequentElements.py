import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            my_map[num] = my_map.get(num,0) + 1
        

        heap = []
        for item in my_map.keys():
            heapq.heappush(heap,(my_map.get(item),item))
            if(len(heap) > k):
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res 

        