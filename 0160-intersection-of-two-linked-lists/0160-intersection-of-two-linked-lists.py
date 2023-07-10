# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2=headA,headB
        has={}
        while l1 is not None:
            has[l1]=1
            l1=l1.next
        while l2 is not None:
            if l2 in has:
                return l2
            l2=l2.next
        return None
                
                