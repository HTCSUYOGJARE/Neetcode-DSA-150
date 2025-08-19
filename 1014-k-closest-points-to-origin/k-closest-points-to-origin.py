class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[]
        for j in points:
            dist = (((j[0])**2)+((j[1])**2))
            heap.append([dist,j])
        heapq.heapify(heap)
        # this gets us the min heap based on the value that is dist. to origin
        res=[]
        for i in range(k):
            point = heapq.heappop(heap)
            res.append(point[1]) 
        return res

# Using simple dictionary migh seem a simpler approach to this but the issue is there are same points repeated multiple times but dictionary only stores 1 unique point and no repeation considered so used heap
         