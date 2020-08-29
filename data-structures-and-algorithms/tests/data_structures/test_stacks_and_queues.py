from data_structures_and_algorithms.data_structures.stacks_and_queues import Stack,Queue


def test_stack_push_1():
    names = Stack()
    names.push("mais")
    actual = names.top.value
    expected ="mais"
    assert actual == expected
# __________________________________________________

def test_stack_push_multiple_values():
    names = Stack()
    names.push("mais")
    names.push("aliaa")
    names.push("fatima")
    actual = names.__str__()
    expected ='<fatima -><aliaa -><mais ->None'
    assert actual == expected
# __________________________________________________

def test_stack_pop():
    names = Stack()
    names.push("mais")
    names.push("aliaa")
    names.push("fatima")
    names.pop()
    actual = names.__str__()
    expected ='<aliaa -><mais ->None'
    assert actual == expected
# __________________________________________________

def test_stack_empty_():
    names = Stack()
    names.push("mais")
    names.push("aliaa")
    names.pop()
    names.pop()
    actual = names.__str__()
    expected ='None'
    assert actual == expected
# __________________________________________________
    
def test_stack_peek():
    names = Stack()
    names.push("mais")
    names.push("aliaa")  
    actual = names.peek()
    expected ="aliaa"
    assert actual == expected
# __________________________________________________
def test_instantiate_empty_stack():
    names = Stack() 
    actual = names.top
    expected =None
    assert actual == expected
# __________________________________________________
def test_errors_empty_stack():
    names = Stack() 
    actual = names.peek()
    expected ='Stack is empty'
    assert actual == expected

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def test_Queues_enqueue_1():
    nums = Queue()
    nums.enqueue(5)
    actual = nums.front.value
    expected =5
    assert actual == expected

# __________________________________________________
def test_enqueue_multiple_values():
    nums = Queue()
    nums.enqueue(5)
    nums.enqueue(22)
    nums.enqueue(777)
    actual = nums.__str__()
    expected ='<5 -><22 -><777 ->None'
    assert actual == expected
# __________________________________________________
def test_dequeue():
    # '<5 -><22 -><777 ->None'
    nums = Queue()
    nums.enqueue(5)
    nums.enqueue(22)
    nums.enqueue(777)
    actual =nums.dequeue()
    expected =5
    assert actual == expected
# __________________________________________________
def test_queue_peek():
    # '<5 -><22 -><777 ->None'
    nums = Queue()
    nums.enqueue(5)
    nums.enqueue(22)
    nums.enqueue(777)
    actual =nums.peek()
    expected =5
    assert actual == expected
# __________________________________________________
def test_multiple_dequeues():
    nums = Queue()
    nums.enqueue(5)
    nums.enqueue(22)
    nums.dequeue()
    nums.dequeue()
    actual =nums.__str__()
    expected = 'None'
    assert actual == expected
# __________________________________________________
def test_empty_queue_exception():
    nums = Queue()
    actual =nums.peek()
    expected ="Empty Queue!:: 'NoneType' object has no attribute 'value'"
    assert actual == expected
# __________________________________________________
def test_instantiate_empty_queue():
    nums = Queue()
    actual =nums.front
    expected = None
    assert actual == expected




