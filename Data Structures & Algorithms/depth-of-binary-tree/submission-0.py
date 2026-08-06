# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr_depth = 0

        return self.find_depth(curr_depth, root)


    
    def find_depth(self, depth, node) -> node:

        if not node:
            return depth
        
        #increment current depth
        depth += 1
        
        return max(self.find_depth(depth, node.left),self.find_depth(depth, node.right))
