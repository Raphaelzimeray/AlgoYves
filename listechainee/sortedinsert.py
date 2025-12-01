""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    node = Node(data)
    prec_node = head
    current_node = head
    count = 0
    while current_node != None and current_node.data < data:
        prec_node = current_node
        current_node = current_node.next
        count +=1
    if count == 0:
        node.next = head
        return node
    node.next = current_node
    prec_node.next = node
    return head
