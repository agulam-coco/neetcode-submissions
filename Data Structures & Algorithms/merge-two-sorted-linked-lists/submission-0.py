# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        curr_pointer = None
        
        
        while list1 and list2:
            #init new node
            new_node = None
            #get list 1 value:
            if list1.val < list2.val:
                new_node = ListNode(list1.val, None)
                list1 = list1.next

            else:
            #get list 2 value 
                new_node = ListNode(list2.val, None)
                list2=list2.next


            #if head is not set, do so
            if not head:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = current.next
        
        #exhaust all lists
        while list1:
            new_node = ListNode(list1.val, None)
            list1 = list1.next

            if not head:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = current.next

        while list2:
            new_node = ListNode(list2.val, None)
            list2 = list2.next

            if not head:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = current.next
        
        return head




