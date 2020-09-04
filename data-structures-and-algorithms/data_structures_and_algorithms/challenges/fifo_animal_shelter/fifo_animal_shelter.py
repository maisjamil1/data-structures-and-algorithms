class Dog:
    """
    this class will create a dog node
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.type = 'dog'

class Cat:
    """
    this class will create a cat node
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.type = 'cat'



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class AnimalShelter :
    def __init__(self):
        self.cats_queue=Queue()
        self.dogs_queue=Queue()

    # _________________________________________________

    def enqueue(self,animal_name,animal_type):
        """
        this method adds a new node to the back of the (cats or dog) queue with an O(1) Time performance
        """
        if animal_type.lower() == 'cat':
            new_animal=Cat(animal_name)

            self.cats_queue.enqueue(new_animal)

        elif animal_type.lower()  == 'dog':
            new_animal=Dog(animal_name)

            self.dogs_queue.enqueue(new_animal)
            
        else :
            return None

    # _________________________________________________

    def dequeue(self,animal_type):
        """
        removes the node from the front of (cats or dog) queue, and returns the node’s value
        """
        
        if animal_type.lower() == 'cat':
            return self.cats_queue.dequeue()

        elif animal_type.lower() == 'dog':
            return self.dogs_queue.dequeue()
        else :
            return None

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Queue:
    """
    this class will create a queue
    """
    def __init__(self):
        self.front = None
        self.rear = None



    # def enqueue(self, value):
    def enqueue(self,new_animal):
        """
        this method adds a new node to the back of the queue with an O(1) Time performance
        """
        node = new_animal
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
  
    animmmals=AnimalShelter()
    animmmals.enqueue('soso','cat')
    animmmals.enqueue('lolo','cat')
    animmmals.enqueue('max','dog')
    animmmals.enqueue('fofo','dog')
    print(f'cats_queue :{animmmals.cats_queue}')
    print(f'dogs_queue :{animmmals.dogs_queue}')
    print(animmmals.dequeue('dog'))
    print(animmmals.dequeue('cat'))
    print(animmmals.dequeue('snake'))