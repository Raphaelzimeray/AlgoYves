from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    # a tester en premier (tests de base avant de rentrer dans mon code)
    if node == None:
        raise Exception("The node should not be none")
    if index < 0:
        raise Exception("The index should be in the range [0..length-1]")
    count = 0
    while node !=None and count < index:
        node = node.next
        count +=1
    if index > count:
        raise Exception("The index should be in the range [0..length-1]")
    return node


    # Your code goes here.


# Version corrigée (Yves)

from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    # a tester en premier (tests de base avant de rentrer dans mon code)
    if node == None:
        raise Exception("The node should not be none")
    if index < 0:
        raise Exception("The index should be in the range [0..length-1]")
    count = 0
    while node !=None and count < index:
        node = node.next
        count +=1
    if node == None:
        raise Exception("The index should be in the range [0..length-1]")
    return node


    # Your code goes here.


# Lien vers le reste des exercices

# https://www.codewars.com/kata/55befc42bfe4d13ab1000007/python
