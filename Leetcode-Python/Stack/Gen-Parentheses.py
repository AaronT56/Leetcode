class Solution:
    def generateParenthesis(n: int) -> list[str]:
        # So we set up conditions that will ONLY give valid solutions. Then we iterate through them using backtracking. Backtracking will go back steps in your algorithm to check all valid solutions.
        # So if n = 3, we will hit the backtrack part of the if statement, and then we will STACK CALLS. So this call will be paused and we move onto the next call. This happens all the way until we reach the return in the first if statement.
        # At that point we go back to the most recent call. So we will hit the stack.pop() in each paused call until we reach the call backtrack(2, 0). Read below.
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(stack)
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res
    # Tip: The (3,0) pop happens inside the second if statement thats why we start again at (2,0) not (3,0). (3,0) was not really a held call just (2,0) so we go back to it. So we go back to when OpenN = 2 and closedN = 0 because that iteration was when openN = 3 and closedN = 0 was called. Then continue from third if statement.
    # So things come in this order. We go back to (2, 0) then we continue our to (2,1) because we are !!!!KEY!!!!!! we are JUST CONTINUING TO THE NEXT IF STATEMENT SO IT BECOMES (2,1). Like we JUST did stack.pop() right, so what comes after pop, the NEXT if statement so now we cycle through that statement.
    # In the next if statement we again call backtrack so it becomes (3,1) and then we satisfy only the openN < closedN condition so we get two closing brackets )) to get to (3,3).
    # Then we go back to (2,1) because that  is finished and notice that we are again finishing the openN < n if statement so we again just move to the next if statement !!!KEY. 
    # This is how it works. I get it now. So essentially every time we pop a ( bracket, we have to move to the next if statement and then backtrack from there until closedN < openN. That's the ey to this algorithm
sol_order = ['((()))','(()())','(())()',]