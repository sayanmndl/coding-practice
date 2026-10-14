
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #iterative method
        if not head:
            return head
        
        #new weaved list of original and copied nodes
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
            
        ptr = head
        
        #link random pointers of new nodes to 
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
            
            
        #unweave list
        ptr_old_list = head
        ptr_next_list = head.next
        head_new= head.next
        
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_next_list.next = ptr_next_list.next.next if ptr_next_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_next_list = ptr_next_list.next
        return head_new