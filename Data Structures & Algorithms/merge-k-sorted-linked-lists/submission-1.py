# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #case of empty
        if not len(lists):
            return None
        
        #loop through all ists and merge them in twos, until only one lsit rmains

        while len(lists) > 1:
            merged_lists = []


            for i in range(0, len(lists), 2 ):
                
                #possibility that second list i smepty
                first = lists[i]
                second = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(self.mergeLists(first, second))
            
            lists = merged_lists        
        return lists[0]
    
    @staticmethod
    def mergeLists(list1, list2) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        temp = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next
        
        #one or the other or both
        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2
        else:
            temp.next = None
        
        return dummy.next



                




