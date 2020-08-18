from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch


def test_Happy_Path():
    actual=BinarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42], 8)
    expected=3
    assert actual == expected


def test__Happy_Path2():
    actual=BinarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42], 13)
    expected=4
    assert actual == expected
    


def test__Expected_failure():
    actual=BinarySearch([0, 0, 0, 0, 0, 0, 0, 0, 0], 13)
    expected=-1
    assert actual == expected


def test__Expected_failure2():
    actual=BinarySearch([], 1)
    expected=-1
    assert actual == expected
    
 

# def test__Edge_Case():

#     actual=BinarySearch([0, 0, 0, 0, 0, 0, 0, 0, 0],' 13')
#     expected='nice error wallah'
#     assert actual == expected
    
