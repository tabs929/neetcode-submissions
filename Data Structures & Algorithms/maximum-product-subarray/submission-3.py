class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = 1;min_p = 1
        res = nums[0]

        for num in nums:
            tmp = max_p
            max_p = max(num , num*max_p , num*min_p)
            min_p = min(num , num*tmp , num*min_p)
            res = max(res,max_p)
        return res