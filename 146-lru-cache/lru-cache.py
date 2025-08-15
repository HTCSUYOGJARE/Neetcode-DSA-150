class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=defaultdict(list)
        self.res=0
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key][1]=self.res
            self.res+=1
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]=[value,self.res]
            self.res+=1
        else:
            if len(self.cache)<self.capacity:
                self.cache[key]=[value,self.res]
                self.res+=1
            else:
                Res=[]
                for i in self.cache:
                    if Res:
                        if Res[1]>=self.cache[i][1]:
                            Res = [i,self.cache[i][1]]
                    else:
                        Res.append(i)
                        Res.append(self.cache[i][1])
                del self.cache[Res[0]]
                self.cache[key]=[value,self.res]
                self.res+=1
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)