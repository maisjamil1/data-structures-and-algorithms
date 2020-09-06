from data_structures_and_algorithms.challenges.find_maximum_binary_tree.find_maximum_binary_tree import BinaryTree,Node
import pytest

def test_1():
    bt = BinaryTree()
    bt.root= Node(1)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    assert bt.find_maximum_value() == 13

def test_2():
    bt = BinaryTree()
    bt.root= Node(-1)
    bt.root.left = Node(-13)
    bt.root.right = Node(-5)
    assert bt.find_maximum_value() == -1

def test_3():
    bt = BinaryTree()
    assert bt.find_maximum_value() == 'the tree is empty'
