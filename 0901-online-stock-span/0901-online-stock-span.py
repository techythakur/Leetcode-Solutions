class StockSpanner:

    def __init__(self):
        self.stack = [(inf, 0)]

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

        '''if len(self.span)==0:
            self.span.append(price)
            return 1
        self.span.append(price)
        i=len(self.span)-2
        count=1
        while i>=0:
            if self.span[-1]<self.span[i]:
                break
            i-=1
            count+=1
        return count'''



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)