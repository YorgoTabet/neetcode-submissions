class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        start = 0
        best = (0, float("inf"))

        for end, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1

            while missing == 0:
                if end - start < best[1] - best[0]:
                    best = (start, end)
                left = s[start]
                need[left] += 1
                if need[left] > 0:
                    missing += 1
                start += 1

        return "" if best[1] == float("inf") else s[best[0]:best[1] + 1]
