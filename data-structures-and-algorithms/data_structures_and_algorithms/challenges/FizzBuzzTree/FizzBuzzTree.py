class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
# __________________________________________________
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
# __________________________________________________
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
# __________________________________________________

    def find_maximum_value(self):
        """ this method will return the maximum value i a tree """
        try :
            tree_li= self.pre_order()
            if tree_li:
                    max_value = tree_li[0]
                    for item in tree_li:
                        if item > max_value:
                            max_value= item
                    return max_value
            else:
                return 'the tree is empty'
        except Exception as err:
            print(err)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

def FizzBuzzTree(tree):
    """
    this method takes a k-ary tree as an argument.it will determine whether or
    not the value of each node is divisible by 3, 5 or both. 

    """
    li=tree.pre_order()# Root->Left->Right
    # return li
    output=[]
    try:
    
        if li:
            for val in li :
                if val%5==0 and val %3==0:
                    output.append('FizzBuzz')
                elif val%3==0:
                    output.append('Fizz')
                elif val%5==0:
                    output.append('Buzz')
                else:
                    output.append(str(val))
            return output
        else:
            return 'the tree is empty'
    except Exception as err:
        return err    
               
    # return output





                





if __name__=='__main__':

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

    # print(f'pre_order {bt.pre_order()}')
    # print(f'in_order {bt.in_order()}')
    # print(f'post_order {bt.post_order()}')
    # print('*'*50)
    # print(bt.find_maximum_value())


    print('*'*50)
    print(FizzBuzzTree(bt))
    print('*'*50)

