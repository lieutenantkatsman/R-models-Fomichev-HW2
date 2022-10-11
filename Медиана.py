class MedianFinder:
    def __init__(self):
        self.list_ = {}
    def addNum(self, a):
        list_tmp = list(self.list_)
        list_tmp.append(a)
        self.list_ = list_tmp
        # print(self.list_)
        return self
    def findMedian(self):
        list_tmp = list(self.list_)
        list_tmp.sort()
        # print(list_tmp)
        if len(list_tmp) % 2 == 1:
            return list_tmp[int(len(list_tmp) / 2)]
        elif len(list_tmp) == 0:
            return 0
        else:
            return ((list_tmp[int(len(list_tmp) / 2)] + list_tmp[int(len(list_tmp) / 2) - 1]) / 2)

median_finder = MedianFinder()
print(median_finder.findMedian() == .0)
median_finder.addNum(1)
median_finder.addNum(2)
print(median_finder.findMedian() == 1.5)
median_finder.addNum(100)
median_finder.addNum(1001)
print(median_finder.findMedian() == 50)