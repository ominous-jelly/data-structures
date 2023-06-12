# Function to swap nodes in a linked list.
def swap_nodes(input_list, val1, val2):

# Sets 4 variables (1 for val1 node, 1 for val2 node, and 2 for the nodes before those)
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None

# Iteration while loop. Cycle through until node1 = val1.
    while node1 is not None:                        
        if node1.get_value() == val1:               
            break
# If we didn't find val1, that's fine, move down one and set node1_prev to where we just checked.
        node1_prev = node1
        node1 = node1.get_next_node()

# Do the same thing for node2
    while node2 is not None:
        if node2.get_value() == val2:               
            break                                   
        node2_prev = node2
        node2 = node2.get_next_node()

# Edge case handling: what if the searched value isn't in the linked list?
    if (node1 == None or node2 == None):
        print("Searched number not found")
        return

# Run a conditional to see if node1 was a head. If so, just put node2 there, it's obviously where it needs to go.
    if node1_prev == None:                         
        input_list.head_node = node2
# Otherwise, we gotta make sure whatever was pointing at node1 is now pointing at node2.
    else:
        node1_prev.set_next_node(node2)

# Do the same thing for node2
    if node2_prev == None:                          
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

# Now that whatever was before node1 and node2 have swapped what they're looking at...
# Let's point node1 and node2 at what they're SUPPOSED to be looking at now.
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


# Function to return nth element of a list
def list_nth_last(input_list, n):

# Set variables; a counter, a iteration pointer, an actual pointer
    count = 1
    iter_node = input_list.head_node
    nth_node = None

# This wraps everything in a loop that will run until the iteration pointer
# reaches the end (or is equal to None).
    while iter_node:
        iter_node = iter_node.get_next_node()
# Keep track of how many iterations we've been through. Simple as that.
        count += 1

# Every iteration, check and see if we've gone the desired value of n + 1.
# The +1 is because we need that extra room. If we only check for n, we're gonna
# be too close and return the value of n + 1 anyway.
        if (count >= n + 1):
# Now that we're exactly as far behind as we need, let's go ahead and put our
# actual pointer down at the head.
            if (nth_node is None):
                nth_node = input_list.head_node
# If we've already done that, fine, perfect, just move forward along with the other pointer.
            else:
                nth_node = nth_node.get_next_node()

# This will continue until our iteration node reaches None, in which case, we should
# be set up perfectly to return out actual pointer where we want.
    return nth_node


