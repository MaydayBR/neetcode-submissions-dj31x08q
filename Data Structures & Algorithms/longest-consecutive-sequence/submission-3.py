class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <1:
            return 0
        nums.sort()
        longest = 1
        for i in range(1, len(nums)):
            count=1
            while i < len(nums) and (nums[i] == nums[i-1]+1 or nums[i] == nums[i-1]):
                if nums[i] != nums[i-1]:
                    count+=1
                i+=1
            longest = max(longest, count)
        return longest