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
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        if self.length == 0:
            pass
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1

        return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

            
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        if self.length == 0:
            pass
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
           pass
        elif node is self.tail:
           self.remove_from_tail()
           self.length += 1
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        node.next = self.head
        node.prev = None
        self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            pass
        elif node is self.head:
            self.remove_from_head()
            if node.next is self.tail:
                self.head.next = node
            self.length += 1
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        node.next = None
        node.prev = self.tail
        self.tail = node
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
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
        value = current.value
        if self.length <= 1:
            return value
        while current:
            if current.value > value:
                value = current.value
            current = current.next
        return value

            
