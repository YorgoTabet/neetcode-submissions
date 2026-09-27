class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)} {s}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        offset = 0
        currentLength = ""
        res = []

        while offset < len(s):
            while s[offset] != " ":
                currentLength += s[offset]
                offset += 1
            offset += 1

            res.append(s[offset : offset + int(currentLength)])
            offset += int(currentLength)
            currentLength = ""

        return res

