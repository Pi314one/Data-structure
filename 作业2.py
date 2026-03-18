from _collections_abc import Sequence
from typing import Any

class Set:
    """
    查询，插入，删除
    """
    def __init__(self,iterable: Sequence[Any]) -> None:
        n=len(iterable)
        if n==0:
            self.iterable=[]
        else:
            init=iterable[0]
            self.iterable = [init]
            for i in range(1,n):
                _in=False
                for item in self.iterable:
                    if item == iterable[i]:
                        _in=True
                        break
                if not _in:
                    self.iterable.append(iterable[i])

    def __str__(self)->str:
        """
        在打印时会显示self.iterator
        :return: 类所表示的集合对象
        """
        return str(self.iterable)

    def __contains__(self,item: Any) -> bool:
        """
        检测item是否在集合中
        :param item: 需要检测的对象
        :return: 布尔值
        """
        for i in self.iterable:
            if item == i:
                return True
        return False

    def __getitem__(self,index:int) -> Any:
        """
        规定了集合的索引行为
        :param index: 索引
        :return: 元素
        """
        if index<0 or index>=len(self.iterable):
            raise IndexError
        return self.iterable[index]

    def index(self,item)->int:
        """
        规定了集合的查询行为
        :param item: 需要查询的元素
        :return: 该元素的索引（或报错）
        """
        for i in range(len(self.iterable)):
            if item == self.iterable[i]:
                return i
        raise IndexError

    def __len__(self) -> int:
        """
        规定集合的长度
        :return: 集合长度
        """
        return len(self.iterable)

    def __eq__(self,other) -> bool:
        """
        规定集合之间的相等
        :param other: 另一个对象
        :return: bool
        """
        if not isinstance(other, Set):
            return False
        return self.iterable == other.iterable

    def __setitem__(self,index:int,item:Any) -> None:
        if index<0 or index>=len(self.iterable):
            raise IndexError
        if self.__contains__(item):
            print('error:item already exists')
        else:
            self.iterable[index]=item

    def __delitem__(self,index:int) -> None:
        if index<0 or index>=len(self.iterable):
            raise IndexError
        n=len(self.iterable)
        for i in range(index,n-1):
            self.iterable[i]=self.iterable[i+1]
        self.iterable=self.iterable[:n-1]

    def insert(self,index:int,item:Any) -> str|list:
        if index<0 or index>=len(self.iterable):
            raise IndexError
        if self.__contains__(item):
            print('warning:item already exists')
        else:
            self.iterable.append(True)
            for i in range(len(self.iterable)-1,index,-1):
                self.iterable[i]=self.iterable[i-1]
            self.iterable[index]=item
        return self.iterable

    def append(self,item:Any) -> str|list:
        if self.__contains__(item):
            print('warning:item already exists')
        else:
            self.iterable.append(item)
        return self.iterable

class Incremental:
    """
    支持增删查，所有查找均为二分查找
    """
    def __init__(self,iterable: Sequence[int|float]) -> None:
        self.iterable = []
        for item in iterable:
            self.insert(item)

    def __str__(self)->str:
        """
        规定Incremental实例的字符串表示
        :return: 列表的字符串
        """
        return str(self.iterable)

    def __getitem__(self,index:int) -> int|float:
        """
        增加列的索引
        :param index: 索引值
        :return: 数值
        """
        if index<0 or index>=len(self.iterable):
            raise IndexError
        return self.iterable[index]

    def search(self,item:int|float) -> int:
        """
        二分查找的基函数
        :param item: 需要查找的对象
        :return: item对应的索引或者item的邻近值
        """
        left = 0
        right = len(self.iterable)-1
        m = 0
        while left <= right:
            m = (left + right) // 2
            if self.iterable[m] > item:
                right = m-1
            elif self.iterable[m] < item:
                left = m+1
            else:
                break
        return m

    def __contains__(self,item:Any) -> bool:
        m=self.search(item)
        if self.iterable[m]==item:
            return True
        return False

    def index(self,item:int|float)->int:
        """
        二分查找
        :param item: 查找对象
        :return: 查找结果
        """
        m=self.search(item)
        if self.iterable[m]==item:
            return m
        return -1

    def insert(self,item:int|float) ->  list[int|float]:
        """
        插入数
        :param item: 需要插入的对象
        :return: 插入后数列
        """
        if len(self.iterable)==0:
            self.iterable.append(item)
        else:
            m=self.search(item)
            if self.iterable[m] > item:
                m=m-1
            self.iterable.append(True)
            for i in range(len(self.iterable) - 1, m+1, -1):
                self.iterable[i] = self.iterable[i - 1]
            self.iterable[m+1] = item
        return self.iterable

    def __delitem__(self,index:int) -> None:
        """
        删除
        :param index: 索引
        :return: None
        """
        if index < 0 or index >= len(self.iterable):
            raise IndexError
        n = len(self.iterable)
        for i in range(index, n - 1):
            self.iterable[i] = self.iterable[i + 1]
        self.iterable = self.iterable[:n - 1]

"""
Set和Incremental有一些行为是相似的，可以尝试用父类进一步概括
"""