class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = res = 0
        chars = set()

        for r in range(len(s)):
            while(s[r] in chars):
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            res = max(res, len(chars))

        return res