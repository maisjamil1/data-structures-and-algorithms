from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import BinaryTree,Node,tree_intersection


def test_1():
    bt1 = BinaryTree()
    bt1.root = Node(150)
    bt1.root.left = Node(250)
    bt1.root.right = Node(100)
    bt1.root.right.left = Node(350)
    bt1.root.right.right = Node(200)
    bt1.root.left.left = Node(75)
    bt1.root.left.right = Node(160)

    bt2 = BinaryTree()
    bt2.root = Node(42)
    bt2.root.left = Node(600)
    bt2.root.right = Node(100)
    bt2.root.right.left = Node(350)
    bt2.root.right.right = Node(200)
    bt2.root.left.left = Node(15)
    bt2.root.left.right = Node(160)
    
    expected = [160, 100, 350, 200]
    actual=tree_intersection(bt1,bt2)

    assert expected==actual


def test_2():
    bt1 = BinaryTree()
    bt1.root = Node(150)
    bt1.root.left = Node(250)

    bt2 = BinaryTree()
    bt2.root = Node(42)
    bt2.root.left = Node(600)
    bt2.root.right = Node(100)
 
    expected = []
    actual=tree_intersection(bt1,bt2)

    assert expected==actual

def test_3():
    bt1 = BinaryTree()


    bt2 = BinaryTree()
    bt2.root = Node(42)

 
    expected = []
    actual=tree_intersection(bt1,bt2)

    assert expected==actual