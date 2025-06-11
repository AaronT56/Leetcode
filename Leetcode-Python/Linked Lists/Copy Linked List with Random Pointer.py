from typing import Optional
class Node:
    def __init__(self, x : int, next : 'Node' = None, random : 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
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