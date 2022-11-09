class StockSpanner:

    def __init__(self):
        self.span=[]
        

    def next(self, price: int) -> int:
        c=1
        s=self.span
        while s and s[-1][0]<=price:
            c+=s.pop()[1]
        s.append((price,c))
        return c

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