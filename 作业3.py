from operator import add
from typing import Any,Hashable
class HashTable(object):
    def __init__(self,size:int=2**10,iterable:list[Hashable]=None):
        """
        This hash table is constructed using sequence chaining,supporting item addition,query,and deletion.
        :param size: the size of the hash table
        :param iterable: the initial items
        """
        self.size=size
        self.table=[None]*size
        for item in iterable:
            idx=hash(item)%size
            self.append(item)

    def __contains__(self,item:Hashable) -> bool:
        """
        Check if an item is in this hash table
        :param item:
        :return:
        """
        idx=hash(item)%self.size
        if self.table[idx]==item:
            return True
        elif isinstance(self.table[idx],set):
            return item in self.table[idx]
        else:
            return False

    def append(self,item:Hashable) -> None:
        """
        Append an item to the hash table
        :param item:
        :return:
        """
        idx=hash(item)%self.size
        if self.table[idx] is None or self.table[idx]==item:
            self.table[idx]=item
        elif isinstance(self.table[idx],set):
            self.table[idx].add(item)
        else:
            self.table[idx]={self.table[idx],item}

    def __delitem__(self,item:Hashable) -> None:
        """
        Delete an item from the hash table
        :param item:
        :return:
        """
        idx=hash(item)%self.size
        if self.table[idx]==item:
            self.table[idx]=None
        elif isinstance(self.table[idx],set):
            self.table[idx].discard(item)
        else:
            pass