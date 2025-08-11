class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
                    stack.append(int(a/b)) # truncate towards 0 is needed so float is used
        return stack[-1]