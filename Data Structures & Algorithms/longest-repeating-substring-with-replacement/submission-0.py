class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        map = [0] * 26
        maxRec = 0
        CAPITAL_A_ORD = ord("A")

        for p2 in range(len(s)):
            map[ord(s[p2]) - CAPITAL_A_ORD] += 1

            maxRec = max(maxRec, map[ord(s[p2]) - CAPITAL_A_ORD])
            if (p2 - p1 + 1) - maxRec > k:
                map[ord(s[p1]) - CAPITAL_A_ORD] -= 1
                p1 += 1

        return len(s) - p1


"""
abcdzz, k=3.   => 5
map={}, p1=0, p2=0

abcdzz,  usedKs=0, map={a:1}, res = 1
^

abcdzz,  usedKs=1, map={a:1, b:1}, res = 2
^^

abcdzz,  usedKs=2, map={a:1, b:1, c:1}, res = 3
^ ^

abcdzz,  usedKs=3, map={a:1, b:1, c:1, d:1}, res = 4
^  ^

abcdzz,  usedKs=4, map={a:0, b:1, c:1, d:1, z:1}, res = 4
 ^  ^

abcdzz,  usedKs=4, map={a:0, b:1, c:1, d:1, z:2}, res = 4
 ^   ^

"""
