import pytest
from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_1():
    actual=multi_bracket_validation('{}')
    expected=True
    assert actual == expected
    
    # assert "hi" == "hi"

def test_2():
    actual=multi_bracket_validation('{}(){}')
    expected=True
    assert actual == expected

def test_3():
    actual=multi_bracket_validation('()[[Extra Characters]]')
    expected=True
    assert actual == expected

def test_4():
    actual=multi_bracket_validation('(){}[[]]')
    expected=True
    assert actual == expected

def test_5():
    actual=multi_bracket_validation('{}{Code}[Fellows](())')
    expected=True
    assert actual == expected
    
def test_6():
    actual=multi_bracket_validation('[({}]')
    expected=False
    assert actual == expected
    
def test_7():
    actual=multi_bracket_validation('(](')
    expected=False
    assert actual == expected


def test_8():
    actual=multi_bracket_validation('{')
    expected=False
    assert actual == expected

def test_9():
    actual=multi_bracket_validation(')')
    expected=False
    assert actual == expected

def test_10():
    actual=multi_bracket_validation('[}')
    expected=False
    assert actual == expected

def test_11():
    actual=multi_bracket_validation('({)}')
    expected=False
    assert actual == expected