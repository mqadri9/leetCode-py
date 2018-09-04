#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def traverse(nums, res):
            if not nums:
                return
            if len(nums) == 1:
                res.append(nums[0])
                return 
            tmp = nums
            m = max(tmp)
            res.append(m)
            arrleft = tmp[:len(tmp)/2]
            print("--------------------------------------")
            print(arrleft)
            arright = tmp[len(tmp)/2:]
            print(arright)
            if m in arrleft:
                arrleft.remove(m)
            elif m in arright:
                arright.remove(m)
            traverse(arrleft, res)
            traverse(arright, res)
        res = []
        traverse(nums, res)
        return res
