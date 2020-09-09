from data_structures_and_algorithms.challenges.FizzBuzzTree.FizzBuzzTree import Node,BinaryTree,FizzBuzzTree
import pytest

def test_1():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.left = Node(7)
    bt.root.right = Node(5)

    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(15)

    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)

    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    assert FizzBuzzTree(bt).pre_order()==['2', '7', '2', 'Fizz', 'Buzz', '11', 'Buzz', 'Fizz', 'FizzBuzz']

# __________________________________________


def test_2():
    bt = BinaryTree()
    bt.root= Node(-3)
    bt.root.left = Node(-15)
    bt.root.right = Node(-5)
    assert FizzBuzzTree(bt).pre_order() == ['Fizz', 'FizzBuzz', 'Buzz']

# __________________________________________
def test_empty_tree():
    bt = BinaryTree()
    assert FizzBuzzTree(bt) == 'the tree is empty'