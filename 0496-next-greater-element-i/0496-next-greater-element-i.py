class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        vector=[]
        stack=[]
        length=len(nums2)
        for i in range(length-1,-1,-1):
            if not stack:
                vector.append(-1)
                
            elif len(stack)>0 and stack[-1]>nums2[i]:
                vector.append(stack[-1])
                
            elif len(stack)>0 and stack[-1]<=nums2[i]:
                
                while len(stack)>0 and stack[-1]<=nums2[i]:
                    stack.pop()
                    
                if not stack:
                    vector.append(-1)
                else:
                    vector.append(stack[-1])
                    
            stack.append(nums2[i])
            
        vector=vector[::-1]
        
        res=[]
        for i in nums1:
            idx=nums2.index(i)
            res.append(vector[idx])
        return res
            