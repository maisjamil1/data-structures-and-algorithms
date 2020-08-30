class Pseudo_queue:
    def __init__(self):
        self.input =Stack()
        self.output =Stack()
        self.final_output =Stack()

    # _________________________________________________

    def enqueue(self,ele):
        """
        add a node to the end of the stack
        """
        try:
            self.input.push(ele)
            return self.input
        except Exception as err:
            print(f'error ::: {err}')
        
    # _________________________________________________

    def dequeue(self):
        """
        pop a node from the front of the stack
        """
        try:
            curr=self.input.top
            while curr:
                valx=self.input.pop()
                self.output.push(valx.value)
                curr=curr.next

            self.output.pop()

            curr=self.output.top
            while curr:
                valx=self.output.pop()
                self.final_output.push(valx.value)
                curr=curr.next
            return self.final_output
        except Exception as err:
            print(f'error ::: {err}')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

    def __str__(self):
        """
        this method creates a readable output for the user
        """
        try:
            current = self.top
            output = ''
            while current: 
                output += f"-> <{current.value}>"
                current = current.next
            output += f"{current}"
            x=output.replace('None', '')
            return x
        except Exception as err:
            print(f'error ::: {err}')








if __name__ == '__main__':

    print("_"*100)
    ch11 = Pseudo_queue()
    ch11.enqueue(20)
    ch11.enqueue(15)
    ch11.enqueue(10)
    ch11.enqueue(5)
    print(ch11.input)
    print(ch11.dequeue())
    print(ch11.final_output)


    # ________________________________



