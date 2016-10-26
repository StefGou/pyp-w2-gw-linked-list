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
       

    # THIS FUNCTION NEEDED TO RETURN A VALUE E.G. THE TEST_GET_ITEM TEST.
    # BUT WE WERE USING IT TO RETURN A NODE IN THE POP FUNCTION.
    # SO I WAS BREAKING THE POP WHEN I WAS MODIFYING __GETITEM__
    # SO I CREATED THE GET_NODE FUNCTION BELOW IT. NOW EVERYTHING WORKS.
    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError

        wantnode = self.start
        for i in range(index): 
            wantnode = wantnode.next
        return wantnode.elem #ADDED .ELEM TO RETURN THE VALUE
    
    
    def get_node(self, index):
        if index >= len(self):
            raise IndexError

        wantnode = self.start
        for i in range(index): 
            wantnode = wantnode.next
        return wantnode # THIS IS OUR ORIGINAL __GETITEM__ THAT RETURNS A NODE

        
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
    
    
    def __ne__(self, other):
        return not self.__eq__(other)

    
    def __eq__(self, other):
        
        s = self.start
        o = other.start
        
        def is_eq(a, b):
            if not a and not b:
               return True
            if bool(a) == False or bool(b) == False:
                return False
            if a.elem != b.elem:
                return False
            else:
               return is_eq(a.next, b.next)
        
        return is_eq(s, o)
    
    
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
     
        
        if len(self) == 0:
            raise IndexError

        if index != None:
            if index >= len(self):
                raise IndexError
                
        if index == 0 or len(self) == 1:
            to_pop = self.start
            self.start = self.start.next
            return to_pop.elem
        
        if index is None or index == len(self) - 1:
            indextemp = len(self) - 1
            to_pop = self.get_node(indextemp) 
            self.end = self.get_node(indextemp-1)
            self.end.next = None
            return to_pop.elem
        
        else:
            
            to_pop = self.get_node(index)
            #self.__getitem__(indextemp).next = self.__getitem__(len(self) + 1)
            before_to_pop = self.get_node(index-1)
            before_to_pop.next = to_pop.next
            return to_pop.elem
