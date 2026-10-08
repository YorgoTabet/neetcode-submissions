class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substrSet = set(s1)
        map = {}

        for char in s1:
            map[char] = map.get(char, 0) + 1

        l = 0
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                if s2[l] in substrSet:
                    map[s2[l]] = map.get(s2[l], 0) + 1

                    if map[s2[l]] == 0:
                        del map[s2[l]]
                l += 1

            if s2[r] in substrSet:
                map[s2[r]] = map.get(s2[r], 0) - 1
                if map[s2[r]] == 0:
                    del map[s2[r]]

            if len(map.keys()) == 0 and r - l + 1 == len(s1):
                return True

        return False


"""

[]
lecabee, abc

lecabee,  map={a:1, b:1, c:1}
^
lecabee,  map={a:1, b:1, c:1}
^^

lecabee,  map={a:1, b:1}
^ ^

lecabee,  map={b:1}
 ^ ^

lacabee,  map={b:1}
 ^ ^


"""
