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
    def __init__(self, value):
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

# Method to remove a value from the linked list.
    def remove_value(self, value_to_remove):                                # 1. This will take a single value to iterate (or traverse) the list for
        current_node = self.get_head_node()                                 # 2. Sets a "current node" so we know where we're at
        if current_node.get_value() == value_to_remove:                     # 3. Goes ahead and checks the first item in the list first, just in case.
            self.head_node = current_node.get_next_node()                   # 4. If it is the first item, just sets the head node as the next node.
        else:                                                               #
            while current_node:                                             # 5. Otherwise, let's do this for every item in the linked list
                next_node = current_node.get_next_node()                    # 6. Sets a variable that we can use to look at the next node
                if next_node.get_value() == value_to_remove:                # 7. Checks to see if the next node's value is what we're looking for.
                    current_node.set_next_node(next_node.get_next_node())   # 8. If it is, let's set the current node's link to the node after the removed one.
                    current_node = None                                     # 9. Set current node to None (so we can break out of the while loop)
                else:                                                       #
                    current_node = next_node                                # 10. Otherwise, move on to the next

# Method for removing ALL instances of a value from the linked list.
    def remove_all_values(self, value_to_remove):                           
        current_node = self.get_head_node()
        while True:
            if current_node.get_value() == value_to_remove:                 
                self.head_node = current_node.get_next_node()                   
                current_node = self.get_head_node()
            else:
                break
        while current_node:
            next_node = current_node.get_next_node()
            if next_node == None:
                return None
            else:
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                else:
                    current_node = next_node



# Method for returning the node with a certain value (searching the linked list)
    def find_value(self, search_value):
        current_node = self.get_head_node()                                 # 1. Sets the current node
        search_results = []                                                 # 2. Creates an empty list to store the results
        while current_node:                                                 # 
            if current_node.get_value() == search_value:                    # 3. If the current node is equal to the value we're searching for...
                search_results.append(current_node)                         # 4. Pop that hoe in the search results list
            current_node = current_node.get_next_node()                     # 5. Move on to the next, until that shit is worn down.
        return search_results                                               # 6. Return it.




ll = LinkedList(10)
ll.insert_beginning(20)
ll.insert_beginning(30)
ll.insert_beginning(10)
ll.insert_beginning(20)
ll.insert_beginning(10)

ll.remove_all_values(10)
print(ll.stringify_list())

