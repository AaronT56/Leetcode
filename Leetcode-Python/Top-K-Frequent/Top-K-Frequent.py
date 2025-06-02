from collections import Counter
import heapq

class Solution:
    def topKfrequent(self, nums: list[int], k: int) -> list[int]:
        # this counts the frequency of all unique elements in nums
        count = Counter(nums)

        # so this function takes (how many you want to get of something,
        # the list of things you want to do something to, and how you want to
        #do it) we do frequency as the key as otherwise it would just sort the
        # keys in ascending order for the first k elements.
        return heapq.nlargest(k, count.keys(), key = count.get)