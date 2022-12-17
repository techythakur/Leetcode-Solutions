class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif i=="*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i=="-":
                temp1=int(stack.pop())
                temp2=int(stack.pop())
                stack.append(int(temp2)-int(temp1))
            elif i=="/":
                temp1=int(stack.pop())
                temp2=int(stack.pop())
                stack.append(int(temp2/temp1))
            else:
                stack.append(i)
        return int(stack[0])
    
    '''
    stack = []

        for each in tokens:
            #print(stack)
            if each == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif each == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif each == "-":
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                stack.append(int(c2)-int(c1))
            elif each == "/":
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                #print(c2//c1)
                stack.append(int(c2/c1))
            else: 
                stack.append(each)
        return int(stack[0])
    '''
            