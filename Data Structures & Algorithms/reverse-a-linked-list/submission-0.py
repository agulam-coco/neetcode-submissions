# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node_list = None

        while head:
            new_node = ListNode(head.val, node_list)
            node_list = new_node

            head = head.next
            
        return node_list

        