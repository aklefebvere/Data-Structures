"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
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
        pass
        # create instance of ListNode with value
        new_node = ListNode(value)
        
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
            # increment the DLL length attribute
            self.length += 1
        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node
            # increment the DLL length attribute
            self.length += 1
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
        # store the value of the head
        value = self.head.value
        # check if there is a head
        if self.head == None:
            return None
        # delete the head
        # if next is not None
        elif self.head.next:
            # set head.next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head = self.head.next
            # decrement the length of the DLL
            self.length -= 1
        # else (if head.next is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
            # decrement the length of the DLL
            self.length -= 1
        # return the value
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
        # create instance of ListNode with value
        new_node = ListNode(value)
        
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
            # increment the DLL length attribute
            self.length += 1
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node
            # increment the DLL length attribute
            self.length += 1

            
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        value = self.tail.value
        # delete the tail
            # if tail.prev is not None
        if self.tail.prev:
            # set tail.prev's next to None
            self.tail.prev.next = None
            # set tail to tail.prev
            self.tail = self.tail.prev
            # decrement the length of the DLL
            self.length -= 1
        # else (if tail.prev is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None

            self.length -= 1
        # return the value
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if ll is empty or only contains 1 node
        if self.length <= 1:
            return None
        else:
            # if the node that was selected is not the tail
            if node is not self.tail:
                
               # Link the nodes that were on both sides of the
               # selected node together
                
                # set the selected node's next node previous
                # node to the node previous of the selected node
                node.next.prev = node.prev
                # set the selected node's previous next node
                # to the nodes next node
                node.prev.next = node.next

                # make the selcted node the new head

                # set the selected node next node to be
                # the old head
                node.next = self.head
                # set the old head's previous node as the
                # selected node
                self.head.prev = node
                # set the head as the selected node
                self.head = node
            # if the selected node is the tail
            else:
                # set the selected node's previous node's
                # next node as None
                node.prev.next = None
                # make the selected previous node as the new tail
                self.tail = node.prev
                # set the selected node next node to be
                # the head
                node.next = self.head
                # set the old head's previous node as the
                # selected node
                self.head.prev = node
                # set the head as the selected node
                self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length <= 1:
            return None
        else:
            # if node == None:
            #     return None
            if node is not self.head:
                # Link the nodes that were on both sides of the
                # selected node together

                # set the selected node's next node previous
                # node to the node previous of the selected node
                node.next.prev = node.prev
                # set the selected node's previous next node
                # to the nodes next node
                node.prev.next = node.next
            # if the selected node is the tail
            else:
                # if the length of list == 2,
                # flips the head and tail
                if self.head.next is self.tail:
                    self.remove_from_head()
                    self.length += 1
                else: 
                    # if node.next is not the tail,
                    # remove the head and replace it with the 
                    # node after the old head   
                    self.head = node.next

            # set the selected node next node to be
            # the tail
            node.next = None
            # set the selected node's previous node as
            # the old tail
            node.prev = self.tail

            self.tail.next = node

            # set the tail as the selected node
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return None
        
        if node is self.head:
            node.next.prev = None
            # set head to head.next
            self.head = node.next
            self.length -= 1
        elif node is self.tail:
            node.prev.next = None
            # set tail to tail.prev
            self.tail = node.prev
            self.length -= 1
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        value = 0
        while current != None:
            if value  < current.value:
                value = current.value
            current = current.next

        return value
