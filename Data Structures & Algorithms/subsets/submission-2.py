class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = [[]]
        for num in nums:
            op+=[[num] + lst for lst in op]
        return op