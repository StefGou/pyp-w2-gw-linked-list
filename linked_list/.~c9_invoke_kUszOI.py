from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        
        self.elements = elements
        
        self.start = None
        self.end = None
        
        if self.elements:
            for element in self.elements:
                self.append(element)
                
    def __str__(self):
        return '[{}]'.format(", ".join(str(p) for p in self.elements)) if self.elements else "[]"


    def __len__(self):
        return self.count()


    def __iter__(self):
        
        x = self.start
        
        while True:
            yield x.elem
            
            if x.next == None:
                break
            
            x = x.next
            
        raise StopIteration


    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        
        wantnode = self.start
        for i in range(index): 
            wantnode = wantnode.next
        return wantnode

    def __add__(self, other):
        #init new list
        n_list = LinkedList()
        if self.elements:
            for element in self.elements:
                n_list.append(element)
        
        if other.elements:    
            for element in other.elements:
                n_list.append(element)
        
        return n_list

    def __iadd__(self, other):
        return self + other
    
        #for element in other:
           # self.append(element)
        #return self
    
    def __ne__(self, other):
        return not self.__eq__(other)

    
    def __eq__(self, other):
        #return str(self) == str(other)
        s = self.start
        o = other.start
        
        def is_eq(a, b):
            if not a and not b:
               return True
        print(self)
                return False
            if a.elem != b.elem:
                return False
            else:
               return is_eq(a.next, b.next)
        
        #return is_eq(s, o)
    
    
    def append(self, elem):
        new_node = Node(elem)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
        
    def count(self):
        if self.start:
            counter = 1
            tempNode = self.start
            while tempNode.next:
                counter += 1
                tempNode = tempNode.next
            return counter
        else:
            return 0

    def pop(self, index=None):
        
        

        #if index == none, then pop last element
        #change new last element to point to none
        
        # [a, b, c]
        # [[a, ->b], [b, -> c], [[c, ->None]]
        # [[a, ->b], [b, ->None]]
        
        
        #remove index (if its none its the last one)
        #change element just before to point to the next (or none)
        
        #pop(1)
        # [a, b, c]
        # [[a, ->b], [b, -> c], [c, -> None]]
        # [[a, ->c], [b, -> None], [c, -> None]]
        
        #if index == None:
        #    index = -1
        #for e in self:
        #    if e.next == self[index].elem:
        #        e.next = self[index].next
        #        
        #        return self[index].elem
        
        if index is None:
            indextemp = len(self) - 1
            to_pop = self.__getitem__(indextemp) 
            self.end = self.__getitem__(indextemp-1)
            self.end.next = None
            return to_pop.elem
        else:
            to_pop = self.__getitem__(index)
            self.__getitem__(indextemp).next = self.__getitem__(len(self) + 1)
            return to_pop.elem
