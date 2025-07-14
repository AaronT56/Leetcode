# Another really clever solution
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        end = size = 0
        res = []
        for i, c in enumerate(s):
            size += 1
            # This keeps track of the last index of all the letter in the
            # current string and saves it to end.
            end = max(end, lastIndex[c])

            # Once we reach that last letter we append to res and reset size
            if i == end:
                res.append(size)
                size = 0
            
        return res