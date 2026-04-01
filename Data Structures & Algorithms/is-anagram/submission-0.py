from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        char_count_s = Counter(s)
        char_count_t = Counter(t)

        for key,value in char_count_s.items():
            if (key not in char_count_t) or (char_count_t[key]!= value):
                return False
        return True
        