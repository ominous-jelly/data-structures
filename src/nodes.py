class Nodes:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

    def set_value(self, value):
        self.value = value

    def get_link_node(self):
        return self.link_node

    def get_value(self):
        return self.value

# Creating nodes (basically a linked list)
bulbasaur = Nodes("grass")
charmander = Nodes("fire")
squirtle = Nodes("water")

bulbasaur.set_link_node(charmander)
charmander.set_link_node(squirtle)

print(bulbasaur.get_link_node().get_value())
print(bulbasaur.get_link_node().get_link_node().get_value())

