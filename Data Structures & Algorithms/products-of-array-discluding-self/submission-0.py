class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        ls = 1
        for num in nums:
            ls*=num
            prefix.append(ls)
        
        postfix = [1] * len(nums)
        rs = 1
        for i in range(len(nums)-1,-1,-1):
            rs*=nums[i]
            postfix[i] = rs
        
        res = []
        for i in range(len(nums)):
            left = prefix[i-1] if i> 0 else 1
            right = postfix[i+1] if i < len(nums)-1 else 1
            res.append(left*right)

        return res