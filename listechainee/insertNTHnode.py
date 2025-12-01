# à refaire
# Tu pourrais aussi essayer de t'arreter un maillon plus tôt afin d'éviter de devoir créer un prec_node. Ca marche aussi bien
#Tu t'arretes au noeud CM (current_node = CM), le noeud précédent l'endroit de l'insertion
# tu fais dans l'ordre :
# 1 : P3 = P2(car P2 pointe sur v4)
# 2 : P2 = M(V3,P3)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_nth(head:Node, index, data):
    node = Node(data)
    if index == 0:
        node.next = head
        return node
    else:
        count = 0
        prec_node = head
        current_node = head
        while current_node !=None and count != index:
            count +=1
            prec_node = current_node
            current_node = current_node.next
        if index != count:
            raise Exception("Index too high")
        node.next = current_node
        prec_node.next = node
        return head
