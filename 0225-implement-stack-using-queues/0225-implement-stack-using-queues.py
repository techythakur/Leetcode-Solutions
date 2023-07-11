class MyStack:

    def __init__(self):
        self.queue1=[]
        self.queue2=[]

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if self.queue1:
            for i in range(len(self.queue1)-1):
                x=self.queue1.pop(0)
                self.queue2.append(x)
            x=self.queue1.pop()
            print(x)
            while self.queue2:
                self.queue1.append(self.queue2.pop(0))
            return x
        return None
        

    def top(self) -> int:
        return self.queue1[-1]
        

    def empty(self) -> bool:
        if self.queue1:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()