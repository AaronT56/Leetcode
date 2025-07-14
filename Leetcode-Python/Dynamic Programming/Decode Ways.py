class Solution:
    def numDecodings(self, s: str) -> int:
        # Once we reach the end, there is only one way remaining possibility of
        dp = {len(s) : 1}
        def dfs(i):
            # This is to make sure we do not do repeated work. If we already have
            # computed this dp[i] in a previous step, no need to repeat work. 
            # We will use this quite a lot. We will go through our first recursion
            # path and save a lot of the values to this dp dictionary. On the way
            # back we will encounter the same values again and again. It's important
            # to have this saved so we can quickly and efficiently call these.
            if i in dp:
                return dp[i]
            # If we encounter 0, that's bad because we don't want 02 etc. to be paths.
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] == "0123456"):
                res += dfs(i + 2)
                
            # So once we hit the end of s on the first run through, we can finally start
            # getting to the good part. We save recursively how many way we could have 
            # gotten to s[i:] and store it in dp[i] for later. Recurse backwards until
            # you get final output at dfs(0).
            dp[i] = res
            return res
        return dfs(0)
