class MyQueue:

    def __init__(self):
        self.queue=[]
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        return self.queue.pop(0) if self.queue else None
        

    def peek(self) -> int:
        return self.queue[0] if self.queue else None
        

    def empty(self) -> bool:
        return False if self.queue else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()