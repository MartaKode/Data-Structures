"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev  
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # pass
        # wrap the value in a node
        new_node = ListNode(value)
        # check if the DLL is empty
        if self.head is None and self.tail is None:
            # head and tail points to the new new_node now
            self.head = new_node
            self.tail = new_node
            # update length
            self.length +=1

        # otherwise DLL is not empty
        else:
            # connect the nodes themselves: 
            # new new_node becomes the head
            old_head = self.head
            self.head = new_node
            # new head's next needs to point to the old head
            new_node.next = old_head
            # old head's previous needs to point to the new head
            old_head.prev = new_node 
            # update length
            self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # pass
        # check if DLL is empty 
        if self.head is None and self.tail is None:
            return None
        # check if there is only 1 node
        elif self.head == self.tail: 
            removed_node = self.head.value
            # set head and tail to None
            self.head = None
            self.tail = None
            # update length
            self.length -= 1
            # return the removed node
            return removed_node
        # otherwise more than 1 node
        else:
            removed_node = self.head
            # change removed_node's next's prev to None
            removed_node.next.prev = None
            # update the head to the old head's next
            self.head = removed_node.next
            # update length
            self.length -= 1
            return removed_node.value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # pass
        # wrap value in a node
        new_node = ListNode(value)
        # check if dll is empty
        if self.head is None and self.tail is None:
            # head and tail point to the same node now
            self.head = new_node
            self.tail = new_node
            # update length
            self.length += 1
        # otherwise dll is not empty
        else:
            # old tail's next is new_node
            self.tail.next = new_node
            # new_node's prev is old tail
            new_node.prev = self.tail
            # new_node becomes the tail
            self.tail = new_node
            # update length
            self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # pass
        # check if dll is empty
        if self.head is None and self.tail is None:
            return None
        # check if dll has only 1 node
        elif self.head == self.tail:
            removed_node = self.tail.value
            # set head and tail to None
            self.head = None
            self.tail = None
            # update length
            self.length -= 1
            # return removed node
            return removed_node
        # otherwise dll has more than 1 node
        else:
            removed_node = self.tail
            # new tail is removed_node's prev
            self.tail = removed_node.prev
            # new tail's next is None
            self.tail.next = None
            # update length
            self.length -= 1
            # return removed_node's value
            return removed_node.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # pass
        # check if DLL is empty
        if self.head is None and self.tail is None:
            return None
        # check if DLL has only one node
        elif self.head == self.tail:
            return None
        # check if node is already a head
        elif self.head == node:
            return None
        # otherwise remove the node in question and add it to the head
        else:
            # remove node using delete
            DoublyLinkedList.delete(self, node)
            # add node to head using add_to_head
            DoublyLinkedList.add_to_head(self, node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node): # do it towards the end
        # pass
        # check if DLL is empty
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            return None
        # Is the input node already a tail? -- we're done! 
        elif self.tail == node:
            return None
        # Otherwise: remove the node in question & then add it as the tail
        else:
            # use the delete method to remove the node in question
            DoublyLinkedList.delete(self, node)
            # use add_to_tail to add removed node to the tail
            DoublyLinkedList.add_to_tail(self, node.value)
            

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # pass
        # don't need to traverse; we have access to the `node`
        # check if DLL is empty
        if self.head is None and self.tail is None:
            return None
        # check if DLL has only 1 node
        elif self.head == self.tail:
            # set head and tail to None
            self.head = None
            self.tail = None
            # update length
            self.length -= 1
        # check if node is head 
        elif self.head == node:
            # run remove_from_head -- updated length
            DoublyLinkedList.remove_from_head(self)
        # check if node is tail
        elif self.tail == node:
            # run remove_from_tail -- updates length
            DoublyLinkedList.remove_from_tail(self)

        # othewise DLL has more than 1 node
        else:
            # redirect node's prev and next:
            # node's next points to its prev now `node.next.prev = node.prev`
            node.next.prev = node.prev 
            # node's prev points to its next now `node.prev.next = node.next`
            node.prev.next = node.next
            # update length
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # pass
        # check if DLL is empty
        if self.head is None and self.tail is None:
            return None
        # check if DLL has only one noe
        if self.head == self.tail:
            # return either head's or tail's value
            return self.head.value
        # otherwise DLL has more than 1 node
        else: 
            # set current position as head
            current = self.head
            # set max val
            max_val = current.value
            # start at head and iterate until we reach tail
            while current.next is not None:
                if current.value < current.next.value:
                    max_val = current.next.value
                    current = current.next

                else:
                    max_val = current.value
                    current = current.next

            return max_val


# dll = DoublyLinkedList()
# dll.add_to_tail(1)
# # print(dll.get_max())
# dll.add_to_tail(100)
# # print(dll.get_max())
# dll.add_to_tail(99)
# # print(dll.get_max())
# dll.add_to_tail(101)
# # print(dll.get_max())
# print(dll.head.value)
# print(dll.tail.value)
# dll.move_to_end(dll.head)
# print(dll.head.value)
# print(dll.tail.value)


#'''''''''''''''Lecture Notes''''''''''''''''''
    def delete_new(self, node):
        # is there anything to delete?
        if self.head is None and self.tail is None:
            return
        # check if there's only one node
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # check if the node is the head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # check if the node is the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # otherwise, the node is some node in the middle
        else:
            node.delete()
        # don't forget to decrement the length
        self.length -= 1

    def get_max_new(self):
        # if the list is empty, return None
        if self.head is None and self.tail is None:
            return
        # keep track of the largest value we've seen so far
        max_value = self.head.value
        # traverse the entirety of the linked list
        current = self.head.next
        
        while current is not None:
            # if we see a value > the largest value we've seen so far
            if current.value > max_value:
                # update the largest value
                max_value = current.value
            # update current to point do the next node
            current = current.next
        # return the largest value
        return max_value
