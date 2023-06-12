import ll_algorithms
from os import system

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

class LinkedList():

# When creating a list, the only thing we need to pass it is a value for the head node
    def __init__(self, value):
        self.head_node = Node(value)

# Method to return the head node of the linked list
    def get_head_node(self):
        return self.head_node

# Method to create a way to add items to the beginning of the linked list.
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

# Method to print the values of the linked list.
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

# Method to remove a value from the linked list.
    def remove_value(self, value_to_remove):                               
        current_node = self.get_head_node()                                
        if current_node.get_value() == value_to_remove:                    
            self.head_node = current_node.get_next_node()                  
        else:                                                              
            while current_node:                                            
                next_node = current_node.get_next_node()                   
                if next_node.get_value() == value_to_remove:               
                    current_node.set_next_node(next_node.get_next_node())  
                    current_node = None                                    
                else:                                                       
                    current_node = next_node

# Method for removing ALL instances of a value from the linked list.
    def remove_all_values(self, value_to_remove):                           
        current_node = self.get_head_node()
        if current_node is None: return
        while True:                                                         
            if current_node.get_value() == value_to_remove:
                self.head_node = current_node.get_next_node()
                current_node = self.get_head_node()
            else:
                break
        while current_node:
            next_node = current_node.get_next_node()
            if next_node != None:
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                else:
                    current_node = next_node

# Method for returning the node with a certain value (searching the linked list)
    def find_value(self, search_value):
        current_node = self.get_head_node()                                 
        search_results = []                                                 
        while current_node:                                                 
            if current_node.get_value() == search_value:                    
                search_results.append(current_node)                         
            current_node = current_node.get_next_node()                     
        return search_results                                              

### End of linked list class ###

# Creating a linked list 
values = [10, 20, 30, 40]

ll = LinkedList("temp")
for i in values:
    ll.insert_beginning(i)
ll.remove_value("temp")

print(ll_algorithms.list_middle(ll))


# Cleanup for my own sanity
system("rm -r ./__pycache__/")
