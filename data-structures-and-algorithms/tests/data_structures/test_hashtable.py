from data_structures_and_algorithms.data_structures.hashtable.hashtable import Node,LinkedList,Hashtable
import pytest

def test_add():
    hashTB = Hashtable(50)
    hashTB.sett('tower of god', 'con')
    assert hashTB.get('tower of god').values() == [('tower of god', 'con')]



def test_Retrieving_based_on_key():
    hashTB = Hashtable(50)
    hashTB.sett('tower of god', 'con')
    hashTB.sett('one puch man', 'Sitama')
    assert hashTB.get('one puch man').values() == [('one puch man', 'Sitama')]


def test_returns_null_for_key():
    hashTB = Hashtable(50)
    hashTB.sett('tower of god', 'con')
    hashTB.sett('one puch man', 'Sitama')
    assert hashTB.get('hi') == None

def test_collision():
    hashTB = Hashtable()
    hashTB.sett('silent', '123')
    hashTB.sett('listen', '546')
    assert hashTB.get('listen').values() == [('silent', '123'), ('listen', '546')]

def test_hash_key():
    hashTB = Hashtable()
    assert hashTB.hash('silent') ==157


def test_hash_key2():
    hashTB = Hashtable()
    assert hashTB.hash('Death Note')==148




