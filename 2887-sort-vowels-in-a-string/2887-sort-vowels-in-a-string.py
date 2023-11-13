class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        st = "AEIOUaeiou"
        for i in s:
            if i in st:
                vowels.append(i)
        vowels = sorted(vowels)
        k = 0
        for i in range(len(s)):
            if s[i] in st:
                s = s[:i] + vowels[k] + s[i+1:]
                k+=1
        return s