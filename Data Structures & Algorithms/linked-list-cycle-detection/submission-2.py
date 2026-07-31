# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        lookup = set()

        while head:
            if head.val != -1 and head in lookup:
                return True

            lookup.add(head)
            head=head.next
        
        return False
        