class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        two=three=five=0
        while len(ugly)<n:
            while ugly[two]*2<=ugly[-1]: two+=1
            while ugly[three]*3<=ugly[-1]: three+=1
            while ugly[five]*5<=ugly[-1]: five+=1
            ugly.append(min(ugly[two]*2,ugly[three]*3,ugly[five]*5))
        return ugly[-1]
        
        '''arr=[]
        cnt=0
        for i in range(1,100000000):
            temp=i
            for j in [2,3,5]:
                while i%j==0:
                    i=i//j
            if i==1:
                arr.append(temp)
                cnt+=1
            if cnt>n:
                break
            
        return arr[n-1]'''