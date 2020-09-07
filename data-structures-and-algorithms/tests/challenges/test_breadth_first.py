from data_structures_and_algorithms.challenges.breadth_first.breadth_first import Queue,Node,BinaryTree
import pytest

def test_1():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.left = Node(7)
    bt.root.right = Node(5)

    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)

    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)

    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    assert bt.breadth_first_traversal() ==[2, 7, 5, 2, 6, 9, 5, 11, 4]

# __________________________________________

def test_2():
    bt = BinaryTree()
    bt.root= Node(-1)
    bt.root.left = Node(-13)
    bt.root.right = Node(-5)
    assert bt.breadth_first_traversal() == [-1, -13, -5]

# __________________________________________
def test_empty_tree():
    bt = BinaryTree()
    assert bt.breadth_first_traversal() == None