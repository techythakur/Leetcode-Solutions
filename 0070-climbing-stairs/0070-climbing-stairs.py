class Solution:
    def climbStairs(self, n: int) -> int:
        fib1 = 1
        fib2 = 1
        
        for i in range(n - 1):
            temp = fib1
            fib1 += fib2
            fib2 = temp
            
        return fib1
        '''if n<=2:
            return n
        prev1=1
        prev2=2
        current=0
        for i in range(2,n):
            current=prev1+prev2
            prev1=prev2
            prev2=current
        return current'''