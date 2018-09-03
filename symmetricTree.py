# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def traverse(bleft, bright):
            if (not bleft and bright) or (not bright and bleft):
                return False
            elif (not bleft and not bright):
                return True
            if bleft.val != bright.val:
                return False
            
            isSym_left = traverse(bleft.left, bright.right)
            isSym_right = traverse(bleft.right, bright.left)
            
            return isSym_left and isSym_right
            
        return traverse(root.left, root.right)
