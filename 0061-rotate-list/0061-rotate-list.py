# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        cur=head
        leng=1
        while cur.next is not None:
            cur=cur.next
            leng+=1
        
        cur.next=head
        k=k%leng
        k=leng-k
        while k:
            cur=cur.next
            k-=1
        head=cur.next
        cur.next=None
        
        return head