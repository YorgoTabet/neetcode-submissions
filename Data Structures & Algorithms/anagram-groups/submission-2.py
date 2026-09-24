class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createHash(s):
            l = [0] * 26
            for value in s:
                l[97 - ord(value)] +=1
            return "".join(str(l))
        map = {}
        for s in strs:
            map[createHash(s)] = []
        
        for index, i in enumerate(strs):
            map[createHash(i)].append(i)

        return [value for value in map.values()]



"""
{
acr: [0]
pots: 
}

[acr] pots tops car

insert index into map[sorted]

"""
        