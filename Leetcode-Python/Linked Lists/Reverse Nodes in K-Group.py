from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def ReverseKGroup(self, head: Optional[ListNode], k: int):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.kGroup(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # Remember, groupPrev.next points at 1 not at 2 or something. That's why this
            # makes sense. groupPrev is currently set to dummy. Side tip: In linked lists
            # the nodes themselves never change, but by creating a dummy node and changing
            # the pointers in the list, you can make the node you put at the start of the 
            # list follow the same "path" as the groupPrev node kind of took. So you can
            # mutate the list dummy is in without changing dummy. 
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # The idea here is that, currently groupPrev is saved to dummy. So if we have
            # a list dummy - 1 - 2 - 3 - 4 - 5, then groupPrev will point to 1 which when
            # the group is reversed (which it already has been) we can go back and re-point
            # the 1 to the next group (kth). I just didn't think about it starting at dummy
            # and instead thought of it as starting at 1 and then groupPrev.next being
            # pointed at 2 which didn't make sense.
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
    
    def kGroup(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        
        return curr
    