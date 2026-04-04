class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.length+=1

    def findMedian(self) -> float:
        if self.length %2 == 0:
            #even
            right_index = self.length // 2
            left_index = (self.length // 2)-1
            return (self.arr[right_index] + self.arr[left_index]) / 2
        else:
            #odd --> return middle element 
            middle_index = self.length // 2
            return self.arr[middle_index]