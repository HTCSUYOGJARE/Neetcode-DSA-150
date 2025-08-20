class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-x for x in count.values()] # want to create a max heap so negate the values
        heapq.heapify(max_heap) #create a ma heapa so that most frequnet is at top
        time=0
        q=deque()
        while max_heap or q:
            time+=1
            if max_heap:
                cnt = 1+heapq.heappop(max_heap) # cnt is already negative so adding 1 to it to reduce it
                if cnt!=0:
                    q.append([cnt,time+n])
            
            if q and q[0][1]==time:
                heapq.heappush(max_heap,q.popleft()[0])

        return time