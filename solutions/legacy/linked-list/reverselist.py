# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head, ptr = None, head
        
        while ptr:
            next_node = ptr.next
            ptr.next = new_head #reversing
            new_head = ptr #for next iteration
            ptr = next_node #move to next node
        
        return new_head