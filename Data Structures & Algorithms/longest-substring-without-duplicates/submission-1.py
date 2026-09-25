class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = m = 0
        chars = set()

        while(r < len(s)):
            while(s[r] in chars):
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            m = max(m, len(chars))
            r+=1
        return m