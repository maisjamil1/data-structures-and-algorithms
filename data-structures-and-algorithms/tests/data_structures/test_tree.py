from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree,BinarySearchTree,Node
import pytest

@pytest.fixture
def prepare_bt():
    bt = BinaryTree(8)
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    return bt

# _________________________________________

@pytest.fixture
def prepare_bst():
    bst = BinarySearchTree(23)
    bst.add(8)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    return bst

# _________________________________________

def test_empty_binary_tree():
    bt = BinaryTree()
    assert bt.root.value == None

# _________________________________________

def test_instantiate_tree_with_single_root_node():
    bt = BinaryTree(1)
    assert bt.root.value == 1

# _________________________________________
def test_add_left_child_and_right_child_to_root_node():
    bt = BinaryTree(1)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    assert bt.root.value == 1
    assert bt.root.left.value == 13
    assert bt.root.right.value == 5

# _________________________________________

def test_bst_add_values(prepare_bst):
    bst = prepare_bst
    assert bst.root.value == 23
    assert bst.root.right.value == 42
    assert bst.root.left.value == 8
    assert bst.root.left.left.value == 4
    assert bst.root.right.left.value == 27
# _________________________________________
def test_find(prepare_bst):
    bst = prepare_bst
    assert bst.contains(23) == True
    assert bst.contains(00000) == False
 
# _________________________________________

def test_preorder_traversal():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.print_depth_first_traversals("preorder") == '1-2-4-5-3-6-7-'
# _________________________________________

def test_inorder_traversal(prepare_bt):
    bt = prepare_bt
    assert bt.print_depth_first_traversals("inorder") == '8-13-9-7-1-5--4-'

# _________________________________________

def test_postorder_traversal(prepare_bt):
    bt = prepare_bt
    assert bt.print_depth_first_traversals("postorder") == '8-9-13-1--4-5-7-'
























# def test_Happy_Path_enqueue():
#     # ch11 = Pseudo_queue()
#     # ch11.enqueue(20)
#     # ch11.enqueue(15)
#     # ch11.enqueue(10)
#     # ch11.enqueue(5)
#     # actual=ch11.input.__str__()
#     # expected='-> <5>-> <10>-> <15>-> <20>'
#     # assert actual == expected
#     assert "hi"=="hi"