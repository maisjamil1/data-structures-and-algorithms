from data_structures_and_algorithms.challenges.merge_sort.merge_sort import merge_Sort,merge,math
import pytest

def test_sort_list():
    li=[8,4,23,42,16,15]
    actual = merge_Sort(li)
    expected =[4, 8, 15, 16, 23, 42]
    assert expected == actual
    
def test_Reverse_sorted():
    li=[20,18,12,8,5,-2]
    actual = merge_Sort(li)
    expected =[-2, 5, 8, 12, 5, -2]
    assert expected == actual

def test_Few_uniques():
    li=[5,12,7,5,5,7]
    actual = merge_Sort(li)
    expected =[5, 5, 5, 7, 7, 7]
    assert expected == actual

def test_Nearly_sorted():
    li=[2,3,5,7,13,11]
    actual = merge_Sort(li)
    expected =[2, 3, 5, 7, 13, 11]
    assert expected == actual
