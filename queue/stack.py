"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# from singly_linked_list import Node
# from singly_linked_list import LinkedList

# Stack: Last In First Out
# uses push and pop [removes the most recent value] methods

#````````1) Using Arrays: ``````````
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         # pass
#         return self.size

#     def push(self, value):
#         # pass
#         # append value to the array
#         self.storage.append(value)
#         # update size to size +1
#         self.size += 1


#     def pop(self):
#         # pass
#         # check if array is not empty
#         if self.size != 0:
#             self.size -= 1
#             return self.storage.pop()


# ````````` 2) Using Linked Lists using tails:``````````
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # pass
        return self.size

    def push(self, value):
        # pass
        # add value 
        self.storage.add_to_tail(value)
        # update size to size +1
        self.size += 1


    def pop(self):
        # pass
        # check if linked list is not empty
        if self.size != 0:
            self.size -= 1
            # remove the most recently added value --> the tail
            return self.storage.remove_tail()

# ````````` 2) Using Linked Lists using heads:``````````
# from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         # pass
#         return self.size

#     def push(self, value):
#         # pass
#         # add value 
#         self.storage.add_to_head(value)
#         # update size to size +1
#         self.size += 1


#     def pop(self):
#         # pass
#         # check if linked list is not empty
#         if self.size != 0:
#             self.size -= 1
#             # remove the most recently added value --> the tail
#             return self.storage.remove_head()

# 3) Question: 
# -- from what I've read, insertion and deletion of an element is easier, faster 
# and more efficient for linked lists than it is for arrays