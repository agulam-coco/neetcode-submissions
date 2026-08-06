# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        #validity check that contain values
        if (q and not p) or (p and not q):
            return False

        #one root is validd but the other is not
        while q1 and q2:
            val1 = q1.popleft()
            val2 = q2.popleft()

            if (val1 and not val2) or (val2 and not val1):
                return False
            
            if val1 and val2:
                if  val1.val != val2.val:
                    return False

                q1.append(val1.left)
                q1.append(val1.right)
                q2.append(val2.left)
                q2.append(val2.right)


        return True
        