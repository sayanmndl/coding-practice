# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        
        def recurse_tree(curr):
            if not curr:
                return False
            
            left = recurse_tree(curr.left)
            right = recurse_tree(curr.right)
        
            mid = curr == p or curr == q
        
            #if either 2 of the three flags are true
            if mid + left + right >= 2:
                self.ans = curr
            
            #if any of the three flags are true
            return mid or left or right
    
        recurse_tree(root)
        return self.ans