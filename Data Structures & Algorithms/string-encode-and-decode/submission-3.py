class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret+=( str(len(word))+"#"+word )
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []

        n = len(s)
        i=0
        num =""
        while i < n:
            if s[i] == "#":
                i+=1
                wrd = s[i:i+int(num)]
                ret.append(wrd)
                i+=int(num)
                num = ""
            else:
                num+=s[i]
                i+=1
                
        return ret