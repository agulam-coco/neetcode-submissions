# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        stack = []

        #build stack
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        #keep buildijng while there are still things in the stack and the stack and head are not pointing to the same thing
        while len(stack) and head is not stack[-1]:

            #save next
            next_ptr = head.next

            #take last of list
            popped_ptr = stack.pop()

            #head points to last
            head.next = popped_ptr

            #move head to last
            head = head.next

            #last points to the secon
            head.next = next_ptr

            #move to second
            head = head.next

            if head == popped_ptr:
                head.next = None
                break
        
        if stack:
            popped_ptr = stack.pop()
            head.next = popped_ptr

        head.next = None




