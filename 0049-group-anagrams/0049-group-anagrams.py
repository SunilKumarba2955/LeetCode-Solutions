class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            t = ''.join(sorted(i))
            # print(t)
            if t not in dic:
                dic[t] = [i]
            else:
                dic[t].append(i)
        return list(dic.values())