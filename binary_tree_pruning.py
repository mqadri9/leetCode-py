# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(root):
            if not root:
                return True

            delleft = traverse(root.left)
            delright = traverse(root.right)
            if delleft:
                root.left = None
            if delright:
                root.right = None
            if delright and delleft and root.val == 0:
                return True
            else:
                return False
        
        traverse(root)
        return root
