class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_nums= [-x for x in nums]
        heapq.heapify(heap_nums)
        while k>0 and heap_nums:
            maxx = -heapq.heappop(heap_nums)
            k-=1
        return maxx