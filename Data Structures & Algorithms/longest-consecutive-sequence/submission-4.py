class Solution:
    from collections import defaultdict
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum = 0
        all_numbers = set(nums)
        for i in range(len(nums)):
            streak = 1
            need = nums[i]+1
            while need in all_numbers:
                need+=1
                streak+=1
            maximum = max(maximum, streak)
        return maximum