class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #non recursive first 
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        l,r = 0,len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            if nums[m] < nums[r]:
                #numbers between m and r are strictly larger than middle
                if target > nums[m] and target < nums[r]:
                    l=m+1
                else:
                    r = m-1
            else:
                #nums[m] > nums[r]
                if target > nums[m] or target < nums[r]:
                    l=m+1
                else:
                    r=m-1

        return -1
