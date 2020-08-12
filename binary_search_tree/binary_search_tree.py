"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal  to the current node's value
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target): # can implement using recursion
        # pass
        # check if the target value is less than the current node's value 
        # if it is, we also want to know if the left child exists
        if target < self.value and self.left is not None:
            # use recursion to restart the cycle and check if the left child contains the value 
            return self.left.contains(target)
        # check if value is equal to the current node's value
        elif target == self.value:
            return True
        # otherwise value is greater than current node
        # so we want to check if there is a right child
        elif self.right is not None:
            # restart the process with recursion to check if the right child contains the target
            return self.right.contains(target)
        # otherwise, BST does NOT contain target
        else:
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        # pass
        # keep track of max value
        max_val = self.value
        
        # while there is a right child
        while self.right is not None:
            # set max value to right childs value
            max_val = self.right.value
            # set self to its right child
            self = self.right  
        # return max_val    
        return max_val

    # Call the function `fn` on the value of each node
    # This method doesn't return anything
    def for_each(self, fn): # 
        # pass
        # call fn on the root nodes value
        fn(self.value)
        # check if there is a right child
        if self.right:
            # restart the process on the right child with recursion 
            self.right.for_each(fn)
        # otherwise there is no right child - we don't care

        # check if there is a left child 
        if self.left:
            # restart the process with recursion on the ledfft child
            self.left.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  

# # ```` my checks `````
# print(bst.contains(8))
# print(bst.get_max())


# 🍝 Spaghetti code


    # def contains(self, target): # can implement using recursion
    #     # pass
    #     # keep track of whether we're returning true or false
    #     contains = False
    #     # check if the target value is less than the current node's value 
    #     # if it is, we also want to know if the left child exists
    #     # so we can check for both!
    #     if target < self.value and self.left is not None:
    #         # # does the current node have a left child? 
    #         # if self.left:
    #             # # check if the left childs value is equal to target
    #             # if self.left.value == target:
    #             #     # contains is True
    #             #     contains = True

    #             # else:
    #         # use recursion to restart the cycle and check if the left child contains the value
    #         return self.left.contains(target)
    #         # # otherwise, doesn't have a left child
    #         # else:
    #         #     # contains is False
    #         #     contains = False

    #     # check if value is equal to the current node's value
    #     elif target == self.value:
    #         # contains is True
    #         contains = True

    #     # otherwise value is greater than or equal to current node's value
    #     elif self.right is not None:
    #         # # check if current node has a right child
    #         # if self.right:
    #         #     # check if the right value is equal to target
    #         #     if self.right.value == target:
    #         #         # contains is True
    #         #         contains = True

    #         #     else:
    #         #         # use recursion to restart the process
    #         return self.right.contains(target)
    #         # # otherwise, current node doesn't have a right child
    #         # else:
    #         #     # contains is False
    #         #     contains = False

    #     return contains



    # def contains(self, target):
    #     # check to see if the target is the the current node's value
    #     if self.value == target:
    #         return True
    #     # check if there is a left leaf and the target is less than the current node's value
    #     if self.left and target < self.value:
    #         # check if the left leaf contains the value
    #         return self.left.contains(target)
    #     # chek if there is a right leaf
    #     if self.right:
    #         # check if the right leaf contains the value
    #         return self.right.contains(target)
    #     # if the target is not the current node's value or the right or left leaf (if they exist), return False
    #     return False