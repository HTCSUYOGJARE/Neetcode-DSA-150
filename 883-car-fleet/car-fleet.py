class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = {pos:(target-pos)/speed for pos,speed in zip(position,speed)}
        sort_pos_time = sorted(pos_time.items(),key = lambda x:x[0],reverse=True)
        times = [v for k,v in sort_pos_time]
        stack = deque()
        stack.append(times[0])
        for t in times:
            if stack and t>stack[-1]:
                stack.append(t)
        return len(stack)

        