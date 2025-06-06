class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = []
        # So the philosophy of this question, is to use a stack to find the most recent,
        # highest temperature. So we create this stack that tracks the index of the added
        # number and the temperature. 
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                # So here we have found the distance between the smaller temp
                # stackI and i, the current temperature being iterated through.
                # As we save the index in the stack, even if elements in between
                # are removed, we can still find the right distance between elements. 
                # If we dont find any intermediaries smaller peaks (like 30,36 between
                # 38 and 40) then its simple, it will just go 4,3,2,1. However if there is
                # and the element 3 and 2 are removed from the stack, it doesn't matter 
                # because we saved the index.
                res[stackI] = i - stackI
            stack.append((t, i))
        return res
        
temperatures = [30,38,30,36,35,40,28]

