from .interface import AbstractLinkedList
from .node import Node


#
#
#   Hi guys, pretty much all tests are passing... but every time something needs to be added (append) it fails.
#   I think the __iter__ function also is failing. Fixing those 2 things should resolve many problems.
#       -Stéphan
#
#




class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        
        self.elements = elements
        
        self.start = None
        self.end = None
        
        if elements:
            for element in elements:
                self.append(element)
                
    def __str__(self):
        return '[{}]'.format(", ".join(str(p) for p in self.elements)) if self.elements else "[]"


    def __len__(self):
        return self.count()


    def __iter__(self):
        #
        #  I think we need to iterate over the NODES not the elements
        #  We need to get all the values of node.elem
        #       -Stéphan
        #
        for x in self.elements:
            yield x


    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        return self.elements[index]


    def __add__(self, other):

        if other.start is None:
            return self
        elif self.start is None:
            return other
        else:
            #
            #   I'm pretty sure we need to iterate over "other"'s nodes and append them to "self". Something like : 
            #    for x in other:
            #        self.append(x)
            #
            #   So append function needs to be fixed.
            #       -Stéphan
            #
            self.end.next = other.start
            return self
        

    def __iadd__(self, other):
        #
        #   This one should look similar to __add__
        #
        pass
    
    def __ne__(self, other):
        return not self.__eq__(other)

    #
    # I decided to have fun and use a recusion function.
    # Actually should have used a loop to loop over all the nodes.
    # Tests are passing... I hope it's fine. :) Learned recursion with a previous teacher.
    #   -Stéphan
    #
    def __eq__(self, other):
        
        if len(self) != len(other):
            return False
        
        s = self.start
        o = other.start
        
        def is_eq(a, b):
            if a != b:
                return False
            elif a is None and b is None:
                return True
            else:
               return is_eq(a.next, b.next)
        
        return is_eq(s, o)
    
    
    def append(self, elem):
        #
        #   Something's wrong here...
        #
        new_node = Node(elem)
        if self.start is None:
            self.start = new_node
            self.end = new_node
            return self.start
        else:
            self.end.next = new_node
            self.end = new_node


    def count(self):
        if not self.elements:
            return 0
        return sum([1 for x in self.elements])

        
    def pop(self, index=None):
        pass
