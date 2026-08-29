class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum ,maxSum = 0,nums[0]

        for num in nums:
            currSum = max(num+currSum,num)
            maxSum = max(maxSum,currSum)
        return maxSum