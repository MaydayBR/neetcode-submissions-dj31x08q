class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        #build up prefix 
        prefix_value = 1
        for num in nums:
            res.append(prefix_value)
            prefix_value*=num
        
        #build up postfix
        postfix_value = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix_value
            postfix_value*=nums[i]
        
        return res