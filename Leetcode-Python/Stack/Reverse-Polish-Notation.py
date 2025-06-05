class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        # I need to take two things and perform
        # the thing after
        operators = ['+', '-', '*', '/']
        for i in tokens:
            # so i wanna take the numbers perform the operation then pop them from the stack and add the result to the stack, then keep going.
            if i in operators:
                if i == '+':
                    out = stack[-1] + stack[-2]
                    
                if i == '-':
                    out = stack[-2] - stack[-1]
                    
                if i == '*':
                    out = stack[-1] * stack[-2]
            
                if i == '/':
                    out = stack[-2] / stack[-1]

                stack.pop()
                stack.pop()
                stack.append(out)

            else:
                stack.append(int(i))
            
        return stack[-1]

obj = Solution()

obj.evalRPN(["1","2","+","3","*","4","-"])