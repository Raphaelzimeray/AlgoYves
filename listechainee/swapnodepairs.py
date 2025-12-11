from preloaded import Node

def swap_pairs(head):
    if head == None:
        return None
    if head.next == None:
        return head
    node_A = head
    node_B = head.next
    node_A.next = node_B.next
    node_B.next = node_A
    head = node_B
    previous_node = node_A
    node_A = node_A.next
    while node_A !=None and node_A.next != None:
        node_B = node_A.next
        node_A.next = node_B.next
        node_B.next = node_A
        previous_node.next = node_B
        previous_node = node_A
        node_A = node_A.next
    return head


# from preloaded import Node

# def swap_pairs(head):
#     if head == None or head.next == None:
#         return head
#     node_A = head
#     head = node_A.next
#     previous_node = None
#     while node_A !=None and node_A.next != None:
#         node_B = node_A.next
#         node_A.next = node_B.next
#         node_B.next = node_A
#         if previous_node !=None:
#             previous_node.next = node_B
#         previous_node = node_A
#         node_A = node_A.next
#     return head
