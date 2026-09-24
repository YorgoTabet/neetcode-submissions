class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            map["".join(sorted(s))] = []
        
        for index, i in enumerate(strs):
            map["".join(sorted(i))].append(i)

        return [value for value in map.values()]



"""
{
acr: [0]
pots: 
}

[acr] pots tops car

insert index into map[sorted]

"""
        