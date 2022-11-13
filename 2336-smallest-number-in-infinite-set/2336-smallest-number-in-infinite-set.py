class SmallestInfiniteSet:

    def __init__(self):
        self.new=[i for i in range(1,1001)]
        

    def popSmallest(self) -> int:
        x=self.new.index(min(self.new))
        return self.new.pop(x)
        

    def addBack(self, num: int) -> None:
        if num not in self.new:
            self.new.append(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)