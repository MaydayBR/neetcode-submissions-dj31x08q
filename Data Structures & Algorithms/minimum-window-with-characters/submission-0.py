class Solution:
    from collections import defaultdict, Counter

    def isvalid(self,curr,need):
        for key,val in need.items():
            if curr[key] < val:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        curr = defaultdict(int)
        smallest_substring_l = float("inf")
        res = ""
        need = Counter(t)
        l=0
        for r in range(len(s)):
            curr[s[r]]+=1
            while self.isvalid(curr,need):
                #Valid -> move left pointer until its not valid
                if r-l+1 < smallest_substring_l:
                    res = s[l:r+1]
                    smallest_substring_l = r-l+1
                curr[s[l]]-=1
                l+=1

        return res