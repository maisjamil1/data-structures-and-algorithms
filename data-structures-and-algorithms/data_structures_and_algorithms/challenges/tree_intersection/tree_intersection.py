def tree_intersection(bt1,bt2):

    common = []
    
    def _walk(node1,node2):
        if node1 is None or node2 is None:
            return 
        
        if node1.value == node2.value:
            common.append(node1.value)

        _walk(node1.left,node2.left)
        _walk(node1.right,node2.right)
    _walk(bt1.root,bt2.root)

    return common

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        """ this method will return an array of the values --> Root->Left->Right"""
        output = []
        def _walk(node):
            if not node:
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return output
    def in_order(self):
        """ this method will return an array of the values --> Left->Root->Right"""
        output = []
        def walk(node):
            if not node:
                return
            walk(node.left) 
            output.append(node.value)
            walk(node.right)
        walk(self.root)
        return output
    def post_order(self):
        """ this method will return an array of the values --> Left->Right->Root"""
        output = []
        def walk(node):
            if not node:
                return
            walk(node.left)
            walk(node.right)
            output.append(node.value)
        walk(self.root)
        return output




if __name__ == "__main__":
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

    print(tree_intersection(bt1,bt2))

