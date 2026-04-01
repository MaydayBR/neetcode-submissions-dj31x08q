class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0,len(s)-1
        while left <= right:
            #make sure both are at a letter
            while left <= right and not s[left].isalnum():
                left+=1
            while left <= right and not s[right].isalnum():
                right-=1
            if left >= right:
                break
            #characters aren't equal
            if not (s[left] == s[right] or s[left].lower() == s[right].lower()):
                return False

            left+=1
            right-=1

        return True