# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
               
        self.max_sum = float('-inf')
        self.max_gain(root)
        
        return self.max_sum
    
    #max gain contribution from a subtree
    def max_gain(self, node):
    
        if not node:
            return 0

        #max sum on the right and left sub-trees
        left_gain = self.max_gain(node.left)
        right_gain = self.max_gain(node.right)

        #sum for every newpath
        newpath = node.val + left_gain + right_gain

        #max sum
        self.max_sum = max(self.max_sum, newpath)

        #return gain
        return max((node.val + max(left_gain, right_gain)),0)
