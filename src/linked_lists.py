# Linked lists are simply nodes linked to one another
    # These can be unidirectional:
        # [x]  --> [y]  --> [z]
    # Or bidirectional:
        # [x] <--> [y] <--> [z]

# The first node in a linked list is known as the 'head node'.
# The last node in a linked list is known as the 'tail node'.

# Begin by creating a Node class that will act as the element for the linked list.

class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    
    def set_value(self, new_value):
        self.value = new_value
    def set_next_node(self, new_node):
        self.next_node = new_node

# Now that our Node class has been created, we have an object that we can put into
# a linked list.

class LinkedList():

# When creating a list, the only thing we need to pass it is a value for the head node
    def __init__(self, value=None):
        self.head_node = Node(value)

# Method to return the head node of the linked list
    def get_head_node(self):
        return self.head_node

# Method to create a way to add items to the beginning of the linked list.
# This is known as the "First in, First out" type of linked list.  1. [x]       2. [y] --> [x]      3. Now, y is the head node.
    def insert_beginning(self, new_value):
        new_node = Node(new_value)                                          # 1. create a new node. 
        new_node.set_next_node(self.head_node)                              # 2. link the new node to the current head node
        self.head_node = new_node                                           # 3. make the new node the new head node

# Method to print the values of the linked list.
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()                                 # 1. Establishes a variable for our current place in the list.
        while current_node:                                                 # 2. A loop that will run until current_node is no longer valid.
            if current_node.get_value() != None:                            # 3. Checks to see if there is a value at this node.
                string_list += str(current_node.get_value()) + "\n"         # 4. If there is, let's add the value to our string (plus a newline)
            current_node = current_node.get_next_node()                     # 5. Moves on to the next node in line (if there is one)
        return string_list                                                  # 6. Returns our cobbled together string.

ll = LinkedList(5)
ll.insert_beginning(24)
ll.insert_beginning(3)

print(ll.stringify_list())
