# Personal Solution (inefficient O(n^2))
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:    
        if len(hand) % groupSize:
            return False

        hand.sort()
        used = [False] * len(hand)
        res = []
        while (len(res) * groupSize != len(hand)):
            level = []
            
            for i in range(len(hand)):
                if used[i] or len(level) == groupSize:
                    continue
                
                if level == []:
                    level.append(hand[i])
                    used[i] = True

                elif len(level) > 0 and hand[i] - 1 == level[-1]:
                    level.append(hand[i])
                    used[i] = True
                #print(len(level), hand[i], level[-1])
            if len(level) != groupSize:
                return False
            
            else:
                res.append(level)
        
        return True if len(res) * groupSize == len(hand) else False

import heapq
from typing import List
# So in this solution (more efficient) we create a minHeap and wait till it is 
# empty. We can just use counter here or do what I did. You can create a minheap
# out of the key values in count, then we start at minimum in minH and iterate through
# to see if we have everything to make a new group (the nice thing about count dict is
# that everything is nicely in order). If we reach a count of 0 on some value, we ensure
# first that there are values below it, and if there are, we simply pop it from heap.
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # So we ran out of values for some number
                    # but if that number isn't the minimum in
                    # our heap, then there is some value before i
                    # which has no values left that are that value + 1
                    # so we must return False
                    if i != minH[0]:
                        return False

                    heapq.heappop(minH)
        
        return True