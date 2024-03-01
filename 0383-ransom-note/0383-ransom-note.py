from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        ran = Counter(ransomNote)
        for i,j in ran.items():
            if i not in mag or j>mag[i]:
                return False
        return True
        