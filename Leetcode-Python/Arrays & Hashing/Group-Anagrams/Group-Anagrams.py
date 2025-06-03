# defaultdict essentially creates a dictionary but you can add new keys to
# the dictionary anytime you like which is good. We find the answer by setting
# this a adding word to each part of the dictionary with tuple(count). Then
# we list out the dictionary with list(ans.values()).

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord('a')] += 1

            ans[tuple(count)].append(word)

        return list(ans.values())