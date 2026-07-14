class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = [[]]
        for i in nums:
            op+=[lst + [i] for lst in op]
        return op