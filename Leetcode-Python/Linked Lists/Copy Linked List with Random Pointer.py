from typing import Optional
class Node:
    def __init__(self, x : int, next : 'Node' = None, random : 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # We initialise with None, None so that we that if we ever have a node that
        # cur.next or cur.random in second loop outputs to None, we can handle that case
        # easily. It is just to intialise the dictionary to be able to handle None cases.
        copyToNode = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copyToNode[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copyToNode[cur]
            copy.next = copyToNode[cur.next]
            copy.random = copyToNode[cur.random]
            cur = cur.next
        
        return copyToNode[head]