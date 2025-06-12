# This is the solution that I kinda mostly came up with but nothing really
# to do with the given solution. This is time-wise very slow need to use heaps
# or something else. I'm gonna just use NeetCode Solution
from typing import Optional, List
class ListNode:
     def __init__(self, val: int, next = None):
          self.val = val
          self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while lists:
            smallest = float("infinity")
            list_i = -1 # Set this to -1 so after we can check if there was a value found
            # in the loop and if not we can end (we will have all None essentially so we stop)
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val <= smallest:
                        list_i = i
                        smallest = lists[i].val
            if list_i == -1:
                break
            
            node.next = lists[list_i]
            lists[list_i] = lists[list_i].next
            node = node.next

        return dummy.next
    
# Proper time efficient solution divide and conquer O(n*log(k)) instead of O(n*k)
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        # This approach reduces the total work by repeatedly merging pairs of sorted linked lists.
        # On each iteration, we go through the list of linked lists two at a time:
        # we merge list[i] and list[i+1] into a new sorted list.
        # After one full pass, the number of lists is halved.
        # We repeat this process until only one fully merged list remains.
        # This approach is similar to how merge sort works and gives us better performance
        # than merging one list at a time.
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                # So this loop will merge each list into a sorted list with the list 
                # adjacent to it. It will repeat until the outer loop ends.
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            # This will essentially half the length of our lists and repeat till
            # just one list remains (len(lists) > 1) is not met anymore. So we just keep
            # doing this mergedLists thing until we have just one list. That's why we have
            # O(n*log(k)) time because we are halving each time the work we have to do.
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = tail = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next