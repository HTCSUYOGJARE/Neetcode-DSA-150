class Solution(object):
    def isValid(self, s):
        stack=deque()
        d={")":"(","]":"[","}":"{"}
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if stack:
                    top=stack.pop()
                    if top!=d[i]:
                        return False
                else:
                    return False
        return (True if len(stack)==0 else False)
            


        