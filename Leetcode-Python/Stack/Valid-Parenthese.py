class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            # Check if each c is open or closed bracket.
            # if closed bracket (in close to open) then
            # we have to see if they have a corresponding
            # left bracket
            if c in closetoOpen:
                # We need there to already be a stack otherwise
                # this is the first element and it has no corresponding
                # opening bracket == False. We also need the opening bracket
                # to be at the top of the stack otherwise it invalidates what we are
                # trying to fine ('([)]') is invalid so this account for that invalidity.
                # If both conditions are met, pop and check. Once all of s has been cycled
                # through, check if stack if empty. If so, this is a valid solution.
                if stack and closetoOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False