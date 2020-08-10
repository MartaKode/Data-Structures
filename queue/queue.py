"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# Queue: First In First Out
# like a waiting line
# enqueue [adds to the end] and dequeue [removes the most recently added (from the end)] methods

# # ------Using Arrays--------
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         # pass
#         return self.size

#     def enqueue(self, value):
#         # pass
#         # add value to the end of array
#         self.storage.append(value)
#         # update size
#         self.size += 1


#     def dequeue(self):
#         # pass
#         # check if array is not empty
#         if self.size != 0:
#             # update size
#             self.size -= 1
#             # remove the oldest added value --> index 0
#             return self.storage.pop(0)


# ------- Using Linked List --------
from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        # pass
        return self.size

    def enqueue(self, value):
        # pass
        # add value to the tail
        self.storage.add_to_tail(value)
        # update size
        self.size += 1


    def dequeue(self):
        # pass
        # check if linked list is not empty
        if self.size != 0:
            # update size
            self.size -= 1
            # remove the oldest added value --> head
            return self.storage.remove_head()

# # ------- Using Stacks --------
# from stack import Stack

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.stack1 = Stack()
#         self.stack2 = Stack()

    
#     def __len__(self):
#         # pass
#         return self.size

#     def enqueue(self, value):
#         # pass
#         # add value to stack1
#         self.stack1.push(value)
#         # update size
#         self.size += 1


#     def dequeue(self):
#         # pass
#         # check if both stacks are empty
#         if len(self.stack2) == 0 and self.size != 0:
#             # while stack1 is not empty 
#             # self.size -= 1
#             while len(self.stack1) != 0:
#             # push stack1 into stack2
#                 value = self.stack1.pop()
#                 self.stack2.push(value)
            
#             return self.stack2.pop()
#         self.size -= 1
#         return self.stack2.pop()
            
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print('size',q.__len__())
# print(q.dequeue())
# print('size',q.__len__())
# print(q.dequeue())
# print('size',q.__len__())
