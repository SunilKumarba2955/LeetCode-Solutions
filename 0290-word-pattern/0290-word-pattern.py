class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split = s.split()
        if len(split)!=len(pattern): return False
        mapS = {}
        mapP = {}
        for i in range(len(pattern)-1, -1, -1):
            term = split.pop()
            if term not in mapS:
                mapS[term]=pattern[i]
            if pattern[i] not in mapP:
                mapP[pattern[i]]=term
            if mapS[term]!=pattern[i]:
                return False
            if mapP[pattern[i]]!=term:
                return False
        return True