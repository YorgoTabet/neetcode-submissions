class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        def createHash(s):
            l = [0] * 26
            for value in s:
                l[ord(value) - ord("a")] +=1
            return l
        
        for s in strs:
            map[tuple(createHash(s))].append(s)

        return [values for values in map.values()]



"""
{
acr: [0]
pots: 
}

[acr] pots tops car

insert index into map[sorted]

"""
        