class MedianFinder:
    def __init__(self):
        self.max_heap = []#大顶堆
        self.min_heap = []#小顶堆

    def add_num(self,num):
        if not self.max_heap:
            self.max_heap.append(num)
        else:
            if num>=self.max_heap[0]:
                p=self.add_to_min(num)
                if p is not None:
                    self.add_to_max(p)
            else:
                p=self.add_to_max(num)
                if p is not None:
                    self.add_to_min(p)

    def add_to_max(self,num):
        if len(self.max_heap) > len(self.min_heap):
            p=self.max_heap[0]
            self.max_heap[0]=num
            i=0
            while i<len(self.max_heap)//2-1:
                if num >= max(self.max_heap[2*i+1],self.max_heap[2*i+2]):
                    break
                if self.max_heap[2*i+1]<self.max_heap[2*i+2]:
                    self.max_heap[i], self.max_heap[2*i+1] = self.max_heap[2*i+1], num
                else:
                    self.max_heap[i], self.max_heap[2*i+2] = self.max_heap[2*i+2], num
            if 2*i+1<len(self.max_heap):
                if num <self.max_heap[2*i+1]:
                    self.max_heap[i], self.max_heap[2*i+1] = self.max_heap[2*i+1], num
            return p
        else:
            self.max_heap.append(num)
            i = len(self.max_heap) - 1
            while i > 0:
                if num > self.max_heap[(i - 1) // 2]:
                    self.max_heap[i], self.max_heap[(i - 1) // 2] = self.max_heap[(i - 1) // 2], num
                    i = (i - 1) // 2
                else:
                    break
        return None

    def add_to_min(self,num):
        if len(self.min_heap)>len(self.max_heap)-1:
            p=self.min_heap[0]
            self.min_heap[0]=num
            i = len(self.min_heap) - 1
            while i <len(self.min_heap)//2-1:
                if num<=min(self.min_heap[2*i+1],self.min_heap[2*i+2]):
                    break
                if self.min_heap[2*i+1]<self.min_heap[2*i+2]:
                    self.min_heap[i], self.min_heap[2*i+1] = self.min_heap[2*i+1], num
                else:
                    self.min_heap[i], self.min_heap[2*i+2] = self.min_heap[2*i+2], num

            if 2*i+1<len(self.min_heap):
                if num>self.min_heap[2*i+1]:
                    self.min_heap[i], self.min_heap[2*i+1] = self.min_heap[2*i+1], num
            return p

        else:
            self.min_heap.append(num)
            i = len(self.min_heap) - 1
            while i > 0:
                if num < self.min_heap[(i - 1) // 2]:
                    self.min_heap[i], self.min_heap[(i - 1) // 2] = self.min_heap[(i - 1) // 2], num
                    i = (i - 1) // 2
                else:
                    break
        return None

    def find_median(self):
        if len(self.max_heap)==len(self.min_heap):
            return (self.max_heap[0]+self.min_heap[0])/2
        return self.max_heap[0]

if __name__ == '__main__':
    arr=[3,1,4,1,5,4,4]
    mdf=MedianFinder()
    for i in arr:
        mdf.add_num(i)
    md=mdf.find_median()
    print(md)