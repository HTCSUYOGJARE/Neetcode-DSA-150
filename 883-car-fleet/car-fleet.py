class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d={}
        for i in range(len(position)):
            d[position[i]]=(target-position[i])/speed[i]
        D = dict(sorted(d.items(),key=lambda x: x[0],reverse=True))
        time_stack=deque()
        for j in D:
            if time_stack:
                if  D[j]>time_stack[-1]:
                    time_stack.append(D[j])
            else:
                time_stack.append(D[j])
        return len(time_stack)