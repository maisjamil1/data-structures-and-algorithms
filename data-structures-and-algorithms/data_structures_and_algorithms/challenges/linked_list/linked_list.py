class Node():
    """
    this class will create a new node  
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    """
    this class will create a linked list 
    """
    def __init__(self):
        self.head = None
    # _________________________________________

    def insert(self, val):
        """
        this method takes any value as an argument and adds a new node with that
        value to the head of the list with an O(1) Time performance.
        """
        try:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        except Exception as err:
            print(f'error line 28 insert_method {err}')
        

    # _________________________________________

    def includes(self, val):
        """
        this method takes any value as an argument and returns
         a boolean result depending on whether that value exists
        as a Node’s value somewhere within the list.
        """
        try:
            current = self.head
            while current.next:
                if current.val==val:
                    return True
                else: current = current.next
            return False
            # if val in make_list(self):
            #     return True
            # else :
            #     return False
        except Exception as err:
            print(f'error line 51 includes_method {err}')
        
    @property
    def make_list(self):
        current = self.head
        li = []
        while current:
            li.append(current.val)
            current = current.next
        return li

    # _________________________________________

    def append(self, val):
        """
        this method fills the linked list with values
        """
        try:
            new_node = Node(val)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
        except Exception as err:
            print(f'error line 78 append_method {err}')
    # _________________________________________

    def __str__(self):
        """
        this method creates a readable output for the user
        """
        try:
            current = self.head
            output = ''
            while current: 
                output += f"<{current.val} ->"
                current = current.next
            output += f"{current}"#it will print none in the end
            return output
        except Exception as err:
            print(f'error line 94 __str__ {err}')


        

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__=="__main__":
    fruits = LinkedList()
    fruits.append('Apple')
    fruits.append('Orange')
    fruits.append('Banana')
    fruits.insert('first')
    print(fruits.includes('Apple'))#true
    print(fruits.includes('mais'))#false
    print(fruits)#<first -><Apple -><Orange -><Banana ->None
    print(fruits.make_list)#['first', 'Apple', 'Orange', 'Banana']

