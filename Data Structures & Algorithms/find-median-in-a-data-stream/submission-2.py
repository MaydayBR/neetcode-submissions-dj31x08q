class MedianFinder:

    def __init__(self):
        #left side is max heap
        self.left = []
        #right side is min heap
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -1*num)

        #elements in right side must always be greater than or equal to left side
        if (self.left and self.right) and (-1* self.left[0] >= self.right[0]):
            node = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right,node)
        #sizes are uneven
        if len(self.left) > len(self.right)+1:
            node = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right , node)
        if len(self.right) > len(self.left) + 1:
            node = heapq.heappop(self.right)
            heapq.heappush(self.left , -1* node)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) /2
        elif len(self.left) > len(self.right):
            return -1 * self.left[0]
        else:
            return self.right[0]
        
        