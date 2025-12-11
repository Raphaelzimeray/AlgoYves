class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def display_list(head):
    if head != None:
        print(head.data, "->", end="")
        display_list(head.next)


def remove_duplicates(head):
    if head == None:
        return None
    #display_list(head)
    print("")
    current_node = head
    while current_node.next!= None:
        if current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return head
