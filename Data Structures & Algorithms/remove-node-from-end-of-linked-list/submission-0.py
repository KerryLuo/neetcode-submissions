# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        trail = head
        top = head
        prev = None

        for _ in range(n):
            top = top.next
        
        while top:
            top = top.next

            prev = trail
            trail = trail.next
        
        if prev:
            prev.next = prev.next.next
            print(prev.val)
            return start
        else:
            return start.next
        

        