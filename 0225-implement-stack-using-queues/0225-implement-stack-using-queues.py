class MyStack:

    def __init__(self):
        self.queue=[]

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            for i in range(len(self.queue)-1):
                self.push(self.queue.pop(0))
            return self.queue.pop(0)
        return None
        

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()