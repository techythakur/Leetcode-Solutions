class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr=[i for i in s]
        stack=[]
        i=0
        while i<len(arr):
            if stack and stack[-1]==arr[i]:
                stack.pop()
            else:
                stack.append(arr[i])
            i+=1
        return "".join(stack)