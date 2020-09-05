class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class BinaryTree(object):

    # def __init__(self):
    def __init__(self, root=None):
        self.root = Node(root)
        # self.root =None
# _______________________________________________

    def preOrder(self, start, traversal):
        """ this method will return an array of the values --> Root->Left->Right"""
        try:
            if start:
                traversal += (str(start.value) + "-")
                traversal = self.preOrder(start.left, traversal)
                traversal = self.preOrder(start.right, traversal)
            return traversal
        except Exception as err:
            print(err)
# _______________________________________________

    def inOrder(self, start, traversal):
        """ this method will return an array of the values --> Left->Root->Right"""
        try :
            if start:
                traversal = self.inOrder(start.left, traversal)
                traversal += (str(start.value) + "-")
                traversal = self.inOrder(start.right, traversal)
            return traversal
        except Exception as err:
            print(err)
# _______________________________________________

    def postOrder(self, start, traversal):
        """ this method will return an array of the values --> Left->Right->Root"""
        try:
            if start:
                traversal = self.postOrder(start.left, traversal)
                traversal = self.postOrder(start.right, traversal)
                traversal += (str(start.value) + "-")
            return traversal
        except Exception as err:
            print(err)
    
# _______________________________________________

    def print_depth_first_traversals(self, traversal_type):
        """this method will print the tree based on the order"""
        try:

            if traversal_type == "preorder":
                return self.preOrder(self.root, "")
            elif traversal_type == "inorder":
                return self.inOrder(self.root, "")
            elif traversal_type == "postorder":
                return self.postOrder(self.root, "")

            else:
                print("Traversal type " + str(traversal_type) + " is not supported.")
                return False
        except Exception as err:
            print(err)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def add(self, new_val):
        """add values to the tree"""
        self.add_helper(self.root, new_val)
# _______________________________________________

    def add_helper(self, current, new_val):
        try:
            if current.value < new_val:
                if current.right:
                    self.add_helper(current.right, new_val)
                else:
                    current.right = Node(new_val)
            else:
                if current.left:
                    self.add_helper(current.left, new_val)
                else:
                    current.left = Node(new_val)
        except Exception as err:
            print(err)

# _______________________________________________

    def contains(self,data) :
        """
        this Method returns a boolean indicating whether or not the value is in the tree at least once
        """
        try:
            if self.root:
                is_found=self._contains(data,self.root)
                if is_found:
                    return True
                return False
            else:
                return None
        except Exception as err:
            print(err)

# _______________________________________________
    def _contains(self,data,cur_node):
        try:
            if data> cur_node.value and cur_node.right:
                return self._contains(data,cur_node.right)
            elif data< cur_node.value and cur_node.left:
                return self._contains(data,cur_node.left)
            if data==cur_node.value:
                return True
        except Exception as err:
            print(err)










if __name__ == "__main__":
    tree = BinaryTree(1)
    # tree.root=Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(f'pre_order {tree.print_depth_first_traversals("preorder")}')
    print(f'in_order {tree.print_depth_first_traversals("inorder")}')
    print(f'post_order {tree.print_depth_first_traversals("postorder")}')

    print('-'*50)

    bst=BinarySearchTree(30)
    bst.add(25)
    bst.add(40)
    bst.add(26)
    bst.add(18)
    bst.add(50)
    bst.add(39)

    print(bst.root.right.value)#40
    print(bst.root.right.left.value)#39
    print(bst.root.right.right.value)#50

    print(bst.root.left.value)#25
    print(bst.root.left.right.value)#26
    print(bst.root.left.left.value)#18


    print(bst.contains(40))#true
    print(bst.contains(1111))#false
    print(bst.contains(30))#true


   

