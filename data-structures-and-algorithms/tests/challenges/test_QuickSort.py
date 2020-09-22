from data_structures_and_algorithms.challenges.QuickSort.QuickSort import QuickSort,Partition,Swap
import pytest

def test_sort_list():
    li=[8,4,23,42,16,15]
    actual = QuickSort(li,0,5)
    expected =[4, 8, 15, 16, 23, 42]
    assert expected == actual
    
def test_Reverse_sorted():
    li=[20,18,12,8,5,-2]
    actual = QuickSort(li,0,5)
    expected =[-2, 5, 8, 12, 18, 20]
    assert expected == actual

def test_Few_uniques():
    li=[5,12,7,5,5,7]
    actual = QuickSort(li,0,5)
    expected =[5, 5, 5, 7, 7, 12]
    assert expected == actual

def test_Nearly_sorted():
    li=[2,3,5,7,13,11]
    actual = QuickSort(li,0,5)
    expected =[2, 3, 5, 7, 11, 13]
    assert expected == actual