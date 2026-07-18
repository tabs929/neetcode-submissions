class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        
        return dp[-1]



        """
        rob1 , rob2 =0,0
        
        #.   |       |
        #.   V       V
        # [rob1,rob2,n,n+1,...]
        for n in nums:
            tmp = max(n + rob1 ,rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2
        """