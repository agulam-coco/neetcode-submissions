# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #Make dummy pointer which points to the first,
        #Have a left and right pointer
        #move the dummy pointer n times.  #set dummy pointer pointee to skip over the nth
        #return dummy's next. that is the head


        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        #get right in position
        while n > 0:
            right = right.next
            n -= 1

        #move left and right till left points to value to be removex
        while right:
            left = left.next
            right = right.next

        #remove the value at tleft
        left.next = left.next.next

        return dummy.next


        