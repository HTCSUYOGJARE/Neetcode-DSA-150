class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # d={}
        # for j in points:
        #     d[tuple(j)] = (((j[0])**2)+((j[1])**2))**(1/2) # key in dict must me immutable and unhashable. so used tuple instead of list
        # # now we have dictionary with point as key(tuple) and value as dist to origin
        heap =[]
        for j in points:
            dist = (((j[0])**2)+((j[1])**2))**(1/2)
            heap.append([dist,j])
        heapq.heapify(heap)
        # this gets us the min heap based on the value that is dist. to origin
        res=[]
        for i in range(k):
            point = heapq.heappop(heap)
            res.append(point[1]) 
        return res