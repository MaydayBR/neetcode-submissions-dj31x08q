class Solution:
    def find(self, l,r,nums):
        if l >= r:
            return nums[l]
        m = (l + r)//2
        if nums[m] < nums[r]:
            return self.find(l,m,nums)
        else:
            return self.find(m+1,r,nums)

    def findMin(self, nums: List[int]) -> int:
        return self.find(0,len(nums)-1,nums)