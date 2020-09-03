from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import Stack,Pseudo_queue,Node
import pytest

def test_Happy_Path_enqueue():
    ch11 = Pseudo_queue()
    ch11.enqueue(20)
    ch11.enqueue(15)
    ch11.enqueue(10)
    ch11.enqueue(5)
    actual=ch11.input.__str__()
    expected='-> <5>-> <10>-> <15>-> <20>'
    assert actual == expected
    # assert "hi"=="hi"

def test_Happy_Path_dequeue():
    ch11 = Pseudo_queue()
    ch11.enqueue(20)
    ch11.enqueue(15)
    ch11.enqueue(10)
    ch11.enqueue(5)
    assert ch11.dequeue()==20

def test_failure1():
    ch11 = Pseudo_queue()
    
    assert ch11.dequeue()==None

def test_failure2():
    ch11 = Pseudo_queue()
    assert ch11.dequeue()==None

def test_Edge_Case():
    ch11 = Pseudo_queue()
    ch11.enqueue("")
    assert ch11.dequeue().__str__()==""

def test_Edge_Case2():
    ch11 = Pseudo_queue()
    ch11.enqueue(None)
    assert ch11.dequeue()==None
