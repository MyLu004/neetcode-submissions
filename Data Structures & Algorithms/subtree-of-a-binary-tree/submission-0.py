# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True
        
        if self.compare(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def compare(self,node,subNode):
        if not node and not subNode:
            return True

        if node and subNode and node.val == subNode.val:
            return self.compare(node.left, subNode.left) and self.compare(node.right, subNode.right)

        else:
            return False 