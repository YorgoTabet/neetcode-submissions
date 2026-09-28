class Solution:
    def isAlphaNum(self, c):
        return len(re.findall(r'([A-Z]|[a-z]|[0-9])', c))
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for i in s:
            if(self.isAlphaNum(i)):
                clean+=i

        if(len(clean) == 0):
            return True

        for index,i in enumerate(clean):
            if(i.lower() != clean[len(clean) - index - 1].lower()):
                return False

        return True