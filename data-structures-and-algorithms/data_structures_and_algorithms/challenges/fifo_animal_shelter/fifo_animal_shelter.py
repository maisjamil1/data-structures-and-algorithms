class Cat:
    def __init__(self,nameC):
        self.name=nameC
        self.type='cat'##to do a check in the dequeue part
        self.next=None



class Dog:
    def __init__(self,nameD):
        self.name=nameD
        self.type='dog'
        self.next=None


class AnimalShelter:
    # The shelter operates using a first-in, first-out approach.
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, animal_name,animal_type):

        if animal_type == 'cat'
            cat = Cat(animal_name)
            if not self.front and not self.rear:
                self.front = cat
                self.rear = cat

            old_rear = self.rear
            self.rear = cat
            old_rear.next = self.rear
        
        if animal_type == 'dog'
            dog = Dog(animal_name)
            if not self.front and not self.rear:
                self.front = dog
                self.rear = dog

            old_rear = self.rear
            self.rear = dog
            old_rear.next = self.rear
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
    animal_1 = AnimalShelter()
    animal_1.enqueue(5)
    enqueue("kera",'cat')
    enqueue("jojo",'cat')
    enqueue("Abbas",'dog')
    print(nums)
    print(nums.__str__())