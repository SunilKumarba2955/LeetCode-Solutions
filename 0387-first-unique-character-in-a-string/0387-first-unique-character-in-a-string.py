class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for ch in s:
            if ch not in seen:
                seen[ch] = 1
            else:
                seen[ch]+=1
        for i in range(len(s)):
            if seen[s[i]]==1:
                return i
        return -1