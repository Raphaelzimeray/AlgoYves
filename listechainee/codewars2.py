from preloaded import Node

# Node is defined in preloaded:
# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None

def length(node: Node) -> int:
    count = 0
    while node != None:
        count +=1
        node = node.next
    return count

def count(node: Node, data) -> int:
    count = 0
    while node !=None:
        if node.data == data:
            count +=1
        node = node.next
    return count
