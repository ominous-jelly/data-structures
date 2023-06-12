# Function to swap nodes in a linked list.
def swap_nodes(input_list, val1, val2):
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None

    while node1 is not None:                        
        if node1.get_value() == val1:               
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == val2:               
            break                                   
        node2_prev = node2
        node2 = node2.get_next_node()

    if (node1 == None or node2 == None):
        print("Searched number not found")
        return

    if node1_prev == None:                         
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev == None:                          
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
    
    return input_list


# Function to return nth element of a list
def list_nth_last(input_list, n):
    count = 1
    iter_node = input_list.head_node
    nth_node = None

    while iter_node:
        iter_node = iter_node.get_next_node()
        count += 1

        if (count >= n + 1):
            if (nth_node is None):
                nth_node = input_list.head_node
            else:
                nth_node = nth_node.get_next_node()
    return nth_node


# Function to return the middle element of a list (left-leaning for even numbers)
def list_middle(input_list):
    fast_pointer = input_list.head_node
    slow_pointer = input_list.head_node

    while fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        slow_pointer = slow_pointer.get_next_node()
        if fast_pointer is not None:
            fast_pointer = fast_pointer.get_next_node()

    return slow_pointer.value
