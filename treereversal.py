# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            traverse(root.right)
            tmp = root.left
            root.left = root.right 
            root.right = tmp
            return
        traverse(root)
        return root
