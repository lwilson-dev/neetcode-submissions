# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next    # remember where we were headed
            curr.next = prev   # flip the arrow backwards
            prev = curr        # prev moves up
            curr = nxt         # curr moves up
        
        return prev
        