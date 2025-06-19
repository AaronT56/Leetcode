class Solution:
    # The approach should be to first find which side is sorted,
    # then after finding that you can find the target in that side
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m

            # So we need to find which half is sorted, so that the interval we are 
            # searching in makes sense. Like if we search the left side but it is not
            # sorted, then when we search we will get like 6 <= target < 3 which means 
            # nothing we aren't even searching. So we find the sorted side, and search
            # that side to see if the target is in the sorted side (then things become)
            # easy. If not we keep searching and move the opposite direction.
            if nums[l] <= nums[m]:
                # Now we find if the target is in the right or left half (we have
                # determined which half is sorted).
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target is in the left half
                else:
                    l = m + 1  # Target is in the right half

            # Right half is sorted
            else:
                # Ok right is sorted, but is target in right, or left?
                # Note the necessity of having <= for nums[r] because it
                # could actually be nums[r].
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target is in the right half
                else:
                    r = m - 1  # Target is in the left half

        return -1
