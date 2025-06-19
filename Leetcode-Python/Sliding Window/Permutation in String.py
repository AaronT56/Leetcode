class Solution:
    def checkInclusion(self, s1 : str, s2: str) -> bool:
        # This is actually a very simple and clean solution. All you have to do is
        # create your two classic arrays and then compare the number of matches between
        # the two arrays. Then once you have your two arrays and how many matches they have
        # at the start. You iterate through the array starting at len(s1) and add one to 
        # the index of our count arrays. Then see if that matches. Then with the left side,
        # you just do the exact opposite until you go through the whole array.
        l = 0
        s1count = [0] * 26
        s2count = [0] * 26
        matches = 0
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            # Note we are only doing the len(s1) in s (not all of s) because we will start
            # our r loop at len(s1) elements into s. So we need to establish their values
            # before we start that loop.
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a') 
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            # This checks if we just lost a match as we just added one so if we take away
            # one from s2count[index] would we have a match? If so matches -= 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s1count[index] += 1

            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] == s2count[index] + 1:
                matches -= 1
            l += 1
        return matches == 26