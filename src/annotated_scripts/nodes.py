# Nodes are the most simple element in complex data structures.

class Nodes:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
# At minimum, a node consists of a value and a pointer to another node. (value and link_node here)
    
# These are methods that will set link nodes and values for the node. By having these two functions
# my nodes have become mutable.

    def set_link_node(self, link_node):
        self.link_node = link_node

    def set_value(self, value):
        self.value = value

# These are methods that will move along the links to find connected nodes. [x] => [y] => [z]
# If I want to move from x to y, I can call x.get_link_node(), and if I want to access y's value
# I can simply call x.get_link_node().get_value() 

    def get_link_node(self):
        return self.link_node

    def get_value(self):
        return self.value

# An example of creating and accessing linked nodes.

bulbasaur = Nodes("grass")
charmander = Nodes("fire")
squirtle = Nodes("water")

bulbasaur.set_link_node(charmander)
charmander.set_link_node(squirtle)

# I have definied my three nodes and linked them together. Now if I want to access charmander's data from
# bulbasaur, I can simply do the following.

print(bulbasaur.get_link_node().get_value())

# I can move further down the linked list as well with this:

#                 charmander      squirtle    squirtle's data
print(bulbasaur.get_link_node().get_link_node().get_value())

