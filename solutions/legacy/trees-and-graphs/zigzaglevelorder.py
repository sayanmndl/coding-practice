# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        level_list=deque()
        
        if not root:
            return res
        
        node_queue = deque([root, None])
        leftorder = True
        
        while len(node_queue)>0:
            curr = node_queue.popleft()
            
            if curr:
                if leftorder:
                    level_list.append(curr.val)
                else:
                    level_list.appendleft(curr.val)
                    
                if curr.left:
                    node_queue.append(curr.left)
                if curr.right:
                    node_queue.append(curr.right)
            else:
                res.append(level_list)
                
                if len(node_queue) > 0:
                    node_queue.append(None)
                    
                level_list = deque()
                leftorder = not leftorder
        return res
                