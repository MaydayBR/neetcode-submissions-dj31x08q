class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()

        maximum_sub = 0
        count = 0

        l = 0
        for i in range(len(s)):
            while s[i] in curr_set:
                element_removed = s[l]
                curr_set.remove(element_removed)
                l+=1

            curr_set.add(s[i])
            maximum_sub = max(maximum_sub, i-l+1)

        return maximum_sub
        
