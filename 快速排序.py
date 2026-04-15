from collections.abc import Sequence
from random import randint

class QuickSort:
    def __init__(self, array: Sequence):
        self.array = array
        self.n=len(array)

    def kernal(self,pivot: int,left: int,right: int):
        self.array[pivot],self.array[left] = self.array[left],self.array[pivot]
        left_pivot=left
        left+=1
        while left <= right:
            if self.array[left] < self.array[left_pivot]:
                self.array[left_pivot],self.array[left] = self.array[left],self.array[left_pivot]
                left+=1
                left_pivot+=1
            elif self.array[left] > self.array[left_pivot]:
                self.array[right],self.array[left]=self.array[left],self.array[right]
                right-=1
            else:
                left+=1
        return left_pivot,left-1


    def quicksort(self,left,right)->Sequence[int|float]:
        if self.n<=1:
            pass
        else:
            pivot=randint(left,right)
            left_pivot,right_pivot=self.kernal(pivot,left,right)
            self.quicksort(left,left_pivot-1)
            self.quicksort(right,right_pivot+1)
        return self.array