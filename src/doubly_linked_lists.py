# These are basically the same thing as linked lists, but the nodes
# that make them up have two pointers instead of just one. One pointer
# points to the previous node and the other points to the next node.
# The head's previous pointer is set to 'null', and the tail's next
# pointer is set to 'null'.

class Node():
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node    
    def set_next_node(self, next_node):
        self.next_node = next_node
    def get_next_node(self):
        return self.next_node
    def set_previous_node(self, previous_node):
        self.previous_node = previous_node
    def get_previous_node(self):
        return self.previous_node
    def get_value(self):
        return self.value

class DoublyLinkedList():
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    
    # Adding to the head of the doubly linked list.
    def add_new_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node
        if current_head is not None:
            current_head.set_previous_node(new_head)
            new_head.set_next_node(current_head)
        self.head_node = new_head
        if self.tail_node == None:
            self.tail_node = current_head

    # Adding to the tail of the doubly linked list.
    def add_new_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node
        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_previous_node(current_tail)
        self.tail_node = new_tail
        if self.head_node == None:
            self.tail_node = new_tail

    # Removing the head of the doubly linked list
    def remove_head(self):
        removed_head = self.head_node
        if removed_head is None:
            return None
        self.head_node = removed_head.get_next_node()
        if self.head_node is not None:
            self.head_node.set_previous_node(None)
        if removed_head == self.tail_node:
            self.remove_tail()
        return removed_head.value

    # Removing the tail of the doubly linked list
    def remove_tail(self):
        removed_tail = self.tail_node
        if removed_tail is None:
            return None
        self.tail_node = removed_tail.get_previous_node()
        if self.tail_node is not None:
            self.tail_node.set_next_node(None)
        
    # Removing by value
    def remove_value(self, target):
        node_to_remove = None
        current_node = self.head_node
        while current_node != None:
            if current_node.value == target:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()
        if node_to_remove == None:
            return None
        elif (node_to_remove == self.head_node):
            self.remove_head()
        elif (node_to_remove == self.tail_node):
            self.remove_tail
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_previous_node()
            next_node.set_previous_node(prev_node)
            prev_node.set_next_node(next_node)
        return node_to_remove

