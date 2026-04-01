class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum = 0
        all_nums = set(nums)
        for num in nums:
            count = 1
            if num-1 not in all_nums:
                #we found a starting point
                next_number = num+1
                while next_number in all_nums:
                    count+=1
                    next_number+=1
            maximum = max(maximum , count)
        return maximum