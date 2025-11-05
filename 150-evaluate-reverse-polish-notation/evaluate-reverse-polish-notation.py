class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= deque()
        for i in tokens:
            if i == "+":
                if stack:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(a)+int(b))
            elif i == "-":
                if stack:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)
            elif i == "*":
                if stack:
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a*b)
            elif i == "/":
                if stack:
                    a=stack.pop()
                    b=stack.pop()
                    val = b/a
                    stack.append(int(val))
            else:
                stack.append(int(i))
        return stack[0]
        