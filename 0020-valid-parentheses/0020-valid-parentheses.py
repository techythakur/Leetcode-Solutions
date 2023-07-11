class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]=='(' and i==')':
                    stack.pop()
                elif stack[-1]=='{' and i=='}':
                    stack.pop()
                elif stack[-1]=='[' and i==']':
                    stack.pop()
                else:
                    stack.append(i)
        return False if stack else True