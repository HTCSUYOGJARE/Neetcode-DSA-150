class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
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
                    stack.append(int(float(a)/b)) # truncate towards 0 is needed so float is used
        return stack[-1]