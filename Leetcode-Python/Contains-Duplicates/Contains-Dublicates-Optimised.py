"""This is similar to the hash solution from twoSum. We don't use the dictionary here because we dont care about the index. So we just use set. Make sure to have the seen.add(num) at the end so that we can save it to the seen set and then check if we have seen that number before. It is O(n) rather than O(n^2) which the brute force method would be."""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False