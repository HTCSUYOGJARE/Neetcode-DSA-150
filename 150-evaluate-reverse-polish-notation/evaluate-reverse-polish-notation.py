class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=deque()
        for i in tokens:
            if (i !="+" and i!="-" and i!="/" and i!="*"):
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                    stack.append(a+b)
                elif i=="-":
                    stack.append(a-b)
                elif i=="*":
                    stack.append(a*b)
                elif i=="/":
                    stack.append(int(float(a)/b))
        return stack[-1]