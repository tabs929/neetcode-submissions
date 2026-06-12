from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        temp =[]

        for key,val in hm.items():
            temp.append([val,key])
        
        temp.sort()

        ans = []
        while len(ans) < k:
            ans.append(temp.pop()[1])

        return ans