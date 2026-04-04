class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, currNums , total):
            if total == target:
                self.res.append(currNums[:])
                return 
            if total > target or i>=len(nums):
                return
            
            #try again will this number
            currNums.append(nums[i])
            dfs(i, currNums , total+nums[i])
            #move onto the next number
            currNums.pop()
            dfs(i+1 , currNums , total)
        
        dfs(0,[],0)
        return self.res