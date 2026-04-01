class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        sorted_strs = []
        for word in strs:
            sorted_strs.append( "".join(sorted(word)) )
        dic = defaultdict(list)

        for i,word in enumerate(sorted_strs):
            dic[word].append(strs[i])
        
        for key,value in dic.items():
            ret.append(value)
        
        return ret