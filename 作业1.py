from typing import Iterable,Any
class Delete:
    def __init__(self,iterable:Iterable[Any])->None:
        """
        把可迭代对象变成可修改的列表
        """
        self.iterable=list(iterable)
    def delete(self,index:int)->list[Any]:
        """
        从第position个位置开始，前一个元素替换为后一个
        :param index: 要删除的元素索引
        :return: 变化后列表不输出最后一项
        """
        n=len(self.iterable)
        for i in range(index, n-1):
            self.iterable[i]=self.iterable[i+1]
        return list(self.iterable[:n - 1])