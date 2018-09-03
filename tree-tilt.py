# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root):
            if not root:
                return 0, 0

            tilt_left, sum_left = traverse(root.left) 
            tilt_right, sum_right = traverse(root.right)

            return abs(sum_left - sum_right) + tilt_left + tilt_right, sum_left + sum_right + root.val
        
        return traverse(root)[0]
