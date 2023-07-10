# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        has={}
        l1=head
        while l1 is not None:
            if l1 not in has:
                has[l1]=1
            else:
                return True
            l1=l1.next
            
        return False