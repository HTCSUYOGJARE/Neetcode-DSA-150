class MinStack(object):

    def __init__(self):
        self.d=[]
        self.extra=[]
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.extra:
            m=min(self.extra[-1],val)
            self.extra.append(m)
        else:
            self.extra.append(val)
        self.d.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.extra.pop()
        self.d.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.d[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.extra[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()