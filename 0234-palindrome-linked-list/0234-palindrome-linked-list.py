# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        l1=head
        while l1 is not None:
            arr.append(l1.val)
            l1=l1.next
        return True if arr==arr[::-1] else False