class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            max_freq = max(count[s[right]],max_freq)

            while (right - left + 1) - max_freq > k:
                count[s[left]]-=1

                if count[s[left]] == 0:
                    del count[s[left]]
                left+=1
                
            ans = max(ans,right - left + 1)

        return ans