class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


    def values(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current=current.next
        return values


# _____________________________________________________
class Hashtable:
    def __init__(self, size=1024):
        self.map = [None]*size
        self.size = size


    def hash(self, key):
        """takes in an arbitrary key and returns an index in the collection."""
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*19 % self.size

# _____________________________________________________

    def sett(self, key, value):
        """his method  hashes the key, and add the key and value pair to the table, handling collisions as needed."""
        hashed_key = self.hash(key)#index

        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key, value))


# _____________________________________________________


    def get(self, key):
        """this method takes in the key and returns the value from the table."""

        index=self.hash(key)
        while self.map[index] !=key:
            if self.map[index] != None:
                return self.map[index]
            else:
                return None

# _____________________________________________________


    def contains(self, key):
        """this method takes in the key and returns a boolean, indicating if the key exists in the table already."""
        value=self.get(key)
        if value:
            return True
        else:
            return False

# _____________________________________________________


if __name__ == "__main__":
    hashTB=Hashtable()
    hashTB.sett('Hunter x Hunter', 'Ghon')
    hashTB.sett('Death Note', 'kira')
    hashTB.sett('one puch man', 'Sitama')
    hashTB.sett('tower of god', 'con')

    hashTB.sett('silent', '123')
    hashTB.sett('listen', '546')

    print(hashTB.hash('silent'))#157
    print(hashTB.hash('listen'))#157
    
    print(f'collision {hashTB.get("listen").values()}')#collision [('silent', '123'), ('listen', '546')]
    print('*'*50)



    print(f'contains==={hashTB.contains("Death Note")}')#true
    print(f'contains==={hashTB.contains("Note")}')#false
    print('+'*50)

    print(f'hash {hashTB.map[hashTB.hash("one puch man")].head.data}')#hash ('one puch man', 'Sitama')


    print('-'*50)
    print(hashTB.get("tower of god").values())#[('tower of god', 'con')]
    print(hashTB.get("tower"))#none
    print('%'*50)
    print( hashTB.get('tower of god'))



