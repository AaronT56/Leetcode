from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                # If we find that something is a palindrome, we append it to part and then
                # we iterate through from j + 1, remember j + 1 represents our upper bound
                # from i. i will be fixed throughout. So essentially when we find a new 
                # palindrome, we pick a new starting point i and then iterate through again
                # with our new upperbound at j + 1 iterating through. 
                # KEY INSIGHT: This algorithm kind of cheats, because every single letter
                # will be a palindrome, hence you will iterate through the string using
                # every single point in the string as a strating point in the palindrome.
                # So no matter what every palindrome will be found. It will still
                # be necessary however, to restart the algorithm after finding each 
                # palindrome, as the path you took to get that palindrome matters.
                # So you must always make sure to start your algorithm again after
                # discovering a new path.
                
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    # We choose to split here. When we find a palindrome, we want to add
                    # that to our res. So in order to split this string, we use our
                    # backtrack function. One key insight for me is that you need to
                    # collect ALL versions of parts. That's why it seems like there might
                    # be repeated work, but actually it's backtracking just like 
                    # any other problem and now seeing if there are any NEW solutions to
                    # add to res after appending the trivial solution.
                    backtrack(j + 1)
                    part.pop()
        backtrack(0)
        return res

    def isPali(self, s, l, r):
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
