class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i,j in pairs:
            dic[i].append(j)
            dic[j].append(i)
        curKey, prevKey = 0,0
        for i in dic.keys():
            if len(dic[i])==1:
                prevKey = i
                curKey = dic[i][0]
                break
        res = [prevKey, curKey]
        while len(dic[curKey])!=1:
            nextKey = dic[curKey][0] if dic[curKey][0]!=prevKey else dic[curKey][1]
            res.append(nextKey)
            prevKey, curKey = curKey, nextKey
        return res
