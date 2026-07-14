class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0) + 1

            while seen[s[right]] > 1:
                seen[s[left]]-=1

                # if seen[s[left]] == 0:
                #     del seen[s[left]]

                left+=1
            max_len = max(max_len, right - left + 1)

        return max_len