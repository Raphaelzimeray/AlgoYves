from binarytree import Node

#Création d'un ABR
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(1)

# Affichage élégant
print(root)


# lien exercices https://www.codewars.com/kata/search/python?q=&r%5B%5D=-6&r%5B%5D=-5&tags=Trees&beta=false&order_by=sort_date%20desc
