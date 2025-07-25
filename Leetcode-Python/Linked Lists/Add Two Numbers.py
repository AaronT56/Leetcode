from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy

        # Carry just brings over the extra one
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else None
            v2 = l2.val if l2 else None

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10 # This removes that annoying as 1 in front of the no. we want.
            cur.next = ListNode(val)

            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
