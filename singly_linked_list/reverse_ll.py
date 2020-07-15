def reverse_ll(ll):
    """
    Recieve a LinkedList as an input and returns a reversed order LL

    Steps:
    1. Each Node needs to point at the prev_node
    2. Head and tail pointers need to be flipped

    Cases:
    1. If the ll is empty return the original that is passed in

    
    """
    # If LL has more than one node
    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        # store a pointer to the current next value
        next_node = current.get_next()

        # switch curent's next pointer to the previous
        current.set_next(previous)

        # increment logic
        previous = current
        current = next_node

    ll.head, ll.tail = ll.tail, ll.head
