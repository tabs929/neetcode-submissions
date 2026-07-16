class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = []
        used = [False] * len(nums)

        def dfs():
            if len(permutations) == len(nums):
                res.append(permutations.copy())
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                permutations.append(nums[i])
                dfs()
                permutations.pop()
                used[i] = False
        dfs()
        return res