class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            # This is just saying, there are too many ) even if we treat all *
            # as (.
            if leftMax < 0:
                return False
            
            # This part is kinda confusing
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0