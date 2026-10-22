class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hm:
                return [hm[diff],i]
            hm[num] = i