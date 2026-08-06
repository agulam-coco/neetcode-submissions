# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.swap_kids(root)

        return root

    def swap_kids(self, node):
        #base case. no need to swap
        if not node:
            return

        #swap child left and child right
        self.swap_kids(node.left)
        self.swap_kids(node.right)

        #swap your left adn right
        temp = node.left
        node.left = node.right
        node.right = temp

        