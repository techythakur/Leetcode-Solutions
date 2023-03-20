class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        
        gap = 1
        for slot in flowerbed:
            if slot == 0:
                gap += 1

                if gap == 3:
                    n -=1
                    gap = 1
                    if n ==0:
                        return True
            
            else:
                gap = 0
        
        if gap == 2:
            n -= 1
        
        return n <= 0
        '''num=0
        for i in range(1,len(flowerbed)):
            if flowerbed[i-1]==flowerbed[i]:
                num+=1
                if flowerbed[i]==1:
                    flowerbed[i]=0
                else:
                    flowerbed[i]=1
        return True if num==n else False'''
                