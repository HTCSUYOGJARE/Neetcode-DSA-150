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
                    stack.append(int(a)+int(b))
                elif i=="-":
                    stack.append(int(a)-int(b))
                elif i=="*":
                    stack.append(int(a)*int(b))
                elif i=="/":
                    stack.append(int(float(a)/int(b)))
        return stack[-1]