class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        freq = Counter(nums)    #dictionary of value(key) = freq
        max_heap = []
        for key,value in freq.items():
            heapq.heappush(max_heap,(-value,key))
        
        for i in range(k):
            pair = heapq.heappop(max_heap)  #(freq, num)
            ret.append(pair[1])

        return ret