class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        d={}
        maxm=0
        for i in range(len(points)-maxm-1):
            i_max=0
            for j in range(i+1,len(points)):
                if (points[j][0]-points[i][0])==0:
                    slope=1000000001
                else:
                    slope= (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                    
                if slope in d.keys():
                    d[slope]+=1
                else:
                    d[slope]=1
                
                i_max=max(i_max,d[slope])
            d.clear()
            maxm=max(maxm,i_max)
        return maxm+1