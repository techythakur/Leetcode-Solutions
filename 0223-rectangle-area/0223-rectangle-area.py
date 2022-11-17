class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        widthA = ax2 - ax1
        heightA = ay2 - ay1
        areaA = widthA * heightA

        widthB = bx2 - bx1
        heightB = by2 - by1
        areaB = widthB * heightB
        
        widthO = max(0, min(ay2, by2) - max(ay1, by1))
        heightO = max(0, min(ax2, bx2) - max(ax1, bx1))
        areaO = widthO * heightO
        
        return areaA + areaB - areaO
        '''def area(x1,y1,x2,y2):
            return (x2-x1)*(y2-y1)
        xOverlap = max(min(ax2,bx2)-max(ax1,bx1), 0)
        yOverlap = max(min(ay2,by2)-max(ay1,by1), 0)
        return area(ax1,ay1,ax2,ay2) + area(bx1,by1,bx2,by2) - xOverlap*yOverlap'''