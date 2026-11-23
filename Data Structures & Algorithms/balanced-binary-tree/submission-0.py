# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        LHeight = self.calculateDepth(root.left)
        RHeight = self.calculateDepth(root.right)

        
        if abs(LHeight - RHeight) > 1 or  abs(-LHeight + RHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def calculateDepth(self,node):
        
        if node is None:
            return 0
        
        LHeight = self.calculateDepth(node.left)
        RHeight = self.calculateDepth(node.right)


        return max(LHeight,RHeight) + 1