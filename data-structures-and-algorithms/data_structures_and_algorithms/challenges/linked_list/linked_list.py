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
    # _________________________________________
    def insertBefore(self, val, newVal):
        """
        this method will add a new node with the given newValue immediately 
        before the given value node
        """
        try:
            current = self.head
            inserted_node = Node(newVal)
            if  self.head==None:
                self.head = inserted_node
            else:
                if self.head.val == val:
                    previous_node = self.head
                    self.head = inserted_node
                    inserted_node.next = previous_node
                    return f"from insertBefore method {newVal}"
                    # pass
                else:
                    current = self.head
                while current.next:
                    if current.next.val == val:
                        previous_node = current.next
                        current.next = inserted_node
                        inserted_node.next = previous_node
                        return f"from insertBefore method {newVal}"
                        #pass
                    else:
                        current = current.next
                return "node is not exist!"
                #pass
        except Exception as err:
            print(f'error line 127 __str__ {err}')
    # _________________________________________
    def insertAfter(self, val, newVal):
        '''
        this method will add a new node with the given newValue immediately after
         the first value node
        '''
        try:
            current = self.head
            inserted_node = Node(newVal)
            if self.head==None:
                    self.head = inserted_node
            else:
                current = self.head
                while current.next :
                    if current.next.val == val:
                        current = current.next
                        previous_node = current.next
                        current.next = inserted_node
                        inserted_node.next = previous_node
                        return f"from insertAfter method {newVal}"
                        # pass
                    else:
                        current = current.next
                        # pass
                        
                return "node is not exist"
        except Exception as err:
            print(f'error line 155 __str__ {err}')
    # _________________________________________
    def kth_from_end(self, k):
        """
            this method takes a number k, as a parameter. Return the node’s value that is k from 
            the end of the linked list. 
        """
        try:
            
            nodes_counter = -1
            current = self.head
            while current != None:
                current = current.next
                nodes_counter = nodes_counter + 1
            if nodes_counter >= k:
                current = self.head
                for i in range(nodes_counter - k):
                    current = current.next

            return current.val


        except:
           return 'value not found'


# +++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__=="__main__":
    fruits = LinkedList()
    fruits.append('Apple')
    fruits.append('Orange')
    fruits.append('Banana')
    fruits.insert('first')
    print(fruits.includes('Apple'))#true
    print(fruits.includes('mais'))#false
    print("-"*50)
    print(fruits)#<first -><Apple -><Orange -><Banana ->None
    print(fruits.make_list)#['first', 'Apple', 'Orange', 'Banana']
    print("-"*50)
    print(fruits.insertBefore('Banana', 'mm'))
    print(fruits.make_list)
    print("-"*50)
    print(fruits.insertAfter('Apple', 'after'))
    print(fruits.make_list)
    print("-"*50)
    print(fruits.kth_from_end(0))
    print(fruits.kth_from_end(2))

