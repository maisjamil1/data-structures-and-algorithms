class Node:
    """
    this class will create a new node
    """
    def __init__(self, value):
        self.value = value
        self.next = None
    # _________________________________________________

class Stack:
    """
    this class will create a stack
    """
    def __init__(self):
        self.top = None
        
    # _________________________________________________

    def push(self, value):
        """
        - Create a node with vlaue
        - Add the node to the top of the stack
         """
        node = Node(value)
        temp = self.top
        self.top = node
        self.top.next = temp
    # _________________________________________________

    def pop(self):

        """
        pop a node from the top of the stack and return the value
        """
        try:
            if self.top:
                first_out = self.top
                self.top = self.top.next
                return first_out
            if not self.top:
                raise Exception('It is an empty stack')
        except Exception as err:
            print(f'error ::: {err}')
        
        # pass
    # _________________________________________________

    def peek(self):
        """
        this method will return the value of the node located on top of the stack

        """
        try:
            return self.top.value
        except AttributeError as e:
            return "Stack is empty"
    # _________________________________________________

    def is_empty(self):
        """
        to check if the stack is empty or not
        """
        try:
            if self.top:
                return False
            else :
                return True
        except Exception as err:
            print(f'error ::: {err}')

    # _________________________________________________

    def __str__(self):
        """
        this method creates a readable output for the user
        """
        try:
            current = self.top
            output = ''
            while current: 
                output += f"<{current.value} ->"
                current = current.next
            output += f"{current}"
            return output
        except Exception as err:
            print(f'error ::: {err}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None



    def enqueue(self, value):
        """
        this method adds a new node to the back of the queue with an O(1) Time performance
        """
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
            return first_node.value
        except Exception as err:
            return "Queue is empty"

    # _________________________________________________
     
    def peek(self):
        """
        this method will return the value of the node located on front of the Queue

        """

        try:
            return self.front.value
        except Exception as err:
            return f"Empty Queue!:: {err}"


    # _________________________________________________
    def is_empty(self):
        """
        to check if the Queue is empty or not
        """
        try:
            if self.front:
                return False #not empty
            else :
                return True #it is empty
        except Exception as err:
            print(f'error ::: {err}')


    # _________________________________________________
    def __str__(self):
        """
        this method creates a readable output for the user
        """
        try:
            current = self.front
            output = ''
            while current: 
                output += f"<{current.value} ->"
                current = current.next
            output += f"{current}"
            return output
        except Exception as err:
            print(f'error ::: {err}')



    





if __name__ == '__main__':
    names = Stack()
    names.push("mais")
    names.push("aliaa")
    names.push("nadin")
    print(names.__str__())
    print("_"*100)
    print(names.peek())
    print("_"*100)
    print(names.__str__())
    print("_"*100)
    names.pop()
    names.pop()
    print(names.__str__())
    print("_"*100)
    names.pop()
    print(names.__str__())
    print(f"is the stack empty ? {names.is_empty()}")
    # ________________________________
    print("__Queue test__"*10)
    nums = Queue()
    print(nums.peek())
    nums.enqueue(5)
    nums.enqueue(1)
    nums.enqueue(8)
    print("_"*100)
    print(nums.__str__())
    print(f"front : {nums.front.value}")
    print(f"rear : {nums.rear.value}")
    print("_"*100)
    print(nums.peek())
    print(f"is the stack empty ? {nums.is_empty()}")
    print("_"*100)
    print(nums.__str__())
    print(nums.dequeue())
    print(nums.__str__())
    print(nums.dequeue())
    print(nums.dequeue())
    print(nums.peek())
    print(f"is the stack empty ? {nums.is_empty()}")
