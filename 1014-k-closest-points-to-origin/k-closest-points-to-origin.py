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