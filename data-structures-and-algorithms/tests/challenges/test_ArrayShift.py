from data_structures_and_algorithms.challenges.ArrayShift.ArrayShift import insertShiftArray

def test_Happy_Path():
    actual=insertShiftArray([2,4,6,8], 5)
    expected=[2,4,5,6,8]
    assert actual == expected


def test__Happy_Path2():
    actual=insertShiftArray([4,8,15,23,42], 16)
    expected=[4,8,15,16,23,42]
    assert actual == expected


def test__Expected_failure():
    actual=insertShiftArray([9,4,6,8], 5)
    expected=[5,9,4,6,8]
    assert actual == expected


def test__Expected_failure2():
    actual=insertShiftArray([1,1,1,1], 5)
    expected=[1,1,1,5,1]
    assert actual == expected

def test__Edge_Case():
    actual=insertShiftArray([0,0,9,9], 5)
    expected=[0,0,5,9,9]
    assert actual == expected
