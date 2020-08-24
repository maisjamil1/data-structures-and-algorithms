from data_structures_and_algorithms.challenges.linked_list.linked_list import LinkedList
from data_structures_and_algorithms import __version__
import pytest


# def test_version():
#     assert __version__ == '0.1.0'


@pytest.fixture
def prepare_data():
    anime = LinkedList()
    node1 = anime.append("BLEACH")
    node2 = anime.append("God of high school")
    node3 = anime.append("Deat note")
    test1= anime.includes("BLEACH")
    test2= anime.includes("Conan")
    return {'anime':anime,"node1":node1,"node2":node2,"node3":node3,"test1":test1,"test2":test2}
# ________________________________________________________________

def test_empty_ll():
    """
    Can the function successfully instantiate an empty linked list?
    """
    expected =LinkedList().__str__()
    actual ='None'
    assert expected == actual

# ________________________________________________________________


def test_insert_ll():
    """
    Can properly insert into the linked list ?
    """
    anime = LinkedList()
    anime.insert("Slam Dunk")
    expected =anime.head.val
    actual ='Slam Dunk'
    assert expected == actual

# ________________________________________________________________
def test_head_ll():
    """
    will The head property point to the first node in the linked list ?
    """
    anime = LinkedList()
    anime.insert("test head")
    expected =anime.head.val
    actual ='test head'
    assert expected == actual

# ________________________________________________________________

def test_insert_multiple_nodes():
    """
    Can properly insert multiple nodes into the linked list ?
    """
    anime = LinkedList()
    anime.insert("Hunter")
    anime.insert("Slam Dunk")
    expected =anime.__str__()
    actual ='<Slam Dunk -><Hunter ->None'
    assert expected == actual

# ________________________________________________________________

def test_include_true(prepare_data):
    """
    Will return true when finding a value within the linked list that exists
    """
    expected =prepare_data['test1'].__str__()
    actual ='True'
    assert expected == actual

# ________________________________________________________________

def test_include_false(prepare_data):
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    expected =prepare_data['test2'].__str__()
    actual ='False'
    assert expected == actual

# ________________________________________________________________
def test_values_in_linked_list(prepare_data):
 
    expected =prepare_data['anime'].__str__()
    actual ='<BLEACH -><God of high school -><Deat note ->None'
    assert expected == actual

# ________________________________________________________________
def test_insertbefore():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertBefore("death note","one puch man")
    assert anime.__str__() == '<Slam dunk -><one puch man -><death note ->None'
# ________________________________________________________________
def test_insertbefore_first_node():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertBefore("Slam dunk","one puch man")
    assert anime.__str__() == '<one puch man -><Slam dunk -><death note ->None'
# ________________________________________________________________
def test_insertAfter_lastnode():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.insertAfter("death note","one puch man")
    assert anime.__str__() == '<Slam dunk -><death note -><one puch man ->None'
# ________________________________________________________________
def test_insertAfter():
    anime = LinkedList()
    anime.append("Slam dunk")
    anime.append("death note")
    anime.append("Naruto")
    anime.insertAfter("death note","one puch man")
    assert anime.__str__() == '<Slam dunk -><death note -><one puch man -><Naruto ->None'






