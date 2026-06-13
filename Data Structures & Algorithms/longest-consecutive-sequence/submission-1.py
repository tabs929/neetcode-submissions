class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset  = set(nums)
        l_seq = 0
        for num in nums:
            #check if its the start
            if num - 1 not in numset:
                length = 0
                while num + length in numset:
                    length+=1
                l_seq = max(l_seq,length)
        return l_seq