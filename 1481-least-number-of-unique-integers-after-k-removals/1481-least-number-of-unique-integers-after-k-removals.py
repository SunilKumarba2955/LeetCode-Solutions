class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        my_dict = {}
        for i in arr:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i]+=1
        freq = my_dict.values()
        freq = sorted(freq)
        # print(freq)
        res = len(freq)
        c = 0
        for j in freq:
            k-=j
            if k<0:
                break
            c+=1
        return res-c