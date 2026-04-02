class Solution:
    def max_freq(self, freq):
        maximum = 0
        for key,value in freq.items():
            maximum = max(maximum,value)
        return maximum


    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        maxf = 0
        res = 0
        for i in range(len(s)):
            freq[s[i]]+=1
            window_length = i-l+1
            max_f = self.max_freq(freq)
            while window_length - max_f > k:
                freq[s[l]]-=1
                l+=1
                window_length-=1
                maxf = self.max_freq(freq)
            res = max(res,window_length)
        return res