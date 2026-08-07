# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #find root, 
        #perform check to see if the tree is a subtree


        q = deque()
        q.append(root)

        #find root of subtree

        curr_val = None
        while q:
            curr_val = q.popleft()
            
            #subroot start found
            if curr_val and curr_val.val == subRoot.val:
                if self.isSame(curr_val, subRoot): 
                    return True

            if curr_val:
                #add sibling nodes
                q.append(curr_val.left)
                q.append(curr_val.right)
        
        #root not foun
        return False

    def isSame(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return self.isSame(root1.left,root2.left) and self.isSame(root1.right, root2.right)
        else:
            return False
        
