from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                searcher = word[:j] + '*' + word[j + 1:]
                nei[searcher].append(word)
        
        visit = set([beginWord])
        res = 1
        q = deque([beginWord])

        while q:
            for p in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    searcher = word[:j] + '*' + word[j + 1:]
                    for neiWord in nei[searcher]:
                        if neiWord not in visit:
                            q.append(neiWord)
                            visit.add(neiWord)
                            
            res += 1
        
        return 0