class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
# __________________________________________________

    # def wrong_breadth_first(self):
    #     """ this method will traverse the input tree using a Breadth-first approach,
    #      and return a list of the values in the tree in the order they were encountered."""
    #     left = []
    #     right = []
    #     def _right(node):
    #         if not node:
    #             return
    #         right.append(node.value)
    #         _right(node.right)         #7 5 -4

    #     _right(self.root)
    #     # ____________________________
    #     def _left(node):
    #         if not node:
    #             return
    #         left.append(node.value)
    #         _left(node.left)            #7 13 8

    #     _left(self.root)
            
    #     final=[]
    #     for i in range(len(left)):
    #         breadth=list((left[i],right[i]))
    #         final.append(breadth)

    #     return final[1:]


    def breadth_first_traversal(self):
            """ this method will traverse the input tree using a Breadth-first approach,
            and return a list of the values in the tree in the order they were encountered."""
            try:
                output = []
                if self.root :
                    tree_queue = Queue()
                    tree_queue.enqueue(self.root)
                    while len(tree_queue)>0:
                        output.append(tree_queue.peek())
                        curr = tree_queue.dequeue()

                        if curr.left:
                            tree_queue.enqueue(curr.left)

                        if curr.right:
                            tree_queue.enqueue(curr.right)
                    return output
                else:
                    print('the tree is empty')
            except Exception as err:
                # return 'the tree is empty'
                print(err)
            


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.values =[]



    def enqueue(self, value):
        """
        this method adds a new node to the back of the queue with an O(1) Time performance
        """
        self.values.insert(0,value)
        node = Node(value)
        # if empty queue
        if not self.front and not self.rear:
            self.front = node
            self.rear = node

        old_rear = self.rear
        self.rear = node
        old_rear.next = self.rear
        
    # _________________________________________________


    def dequeue(self):
        """
        removes the node from the front of the queue, and returns the node’s value
        """
        try:
            first_node = self.front
            self.front = self.front.next
            # return first_node.value
            return self.values.pop()
        except Exception as err:
            return "Queue is empty"

    # _________________________________________________
     
    def peek(self):
        """
        this method will return the value of the node located on front of the Queue

        """

        try:
            return self.values[-1].value
        except Exception as err:
            return f"Empty Queue!:: {err}"
    # _________________________________________________
    def __len__(self):
        return len(self.values)

                





if __name__=='__main__':

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

    print(f'pre_order {bt.pre_order()}')
    print(f'in_order {bt.in_order()}')
    print(f'post_order {bt.post_order()}')
    print('*'*50)
    print(bt.find_maximum_value())


    print('*'*50)
    # print(bt.wrong_breadth_first())
    # print('*'*50)
    print(bt.breadth_first_traversal())
