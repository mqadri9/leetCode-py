# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(root, smallest, second_smallest):
            if not root:
                return second_smallest
            second_smallest = traverse(root.left, smallest, second_smallest)
            second_smallest = traverse(root.right, smallest, second_smallest)
            if root.val < smallest:
                tmp = smallest
                smallest = root.val
                second_smallest = tmp
            elif root.val > smallest and (root.val < second_smallest or second_smallest == -1):
                second_smallest = root.val
            return second_smallest
        
        
        return traverse(root, root.val, -1)
        
