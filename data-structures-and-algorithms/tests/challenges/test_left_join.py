from data_structures_and_algorithms.challenges.left_join.left_join import left_join

def test_1():
    #synonym 
    dict1 = {'fond':'enamored',
    'wrath':'anger',
    'diligent':'employed',
    'outfit':'garb',
    'guide':'usher'}

    #antonym
    dict2 = {'fond':'averse',
    'wrath':'delight',
    'diligent':'idle',
    'guide':'follow',
    'flow':'jam'}
    expected=[['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', None], ['guide', 'usher', 'follow']]
    actual= left_join(dict1,dict2)
    assert expected==actual


def test_2():
    #synonym 
    dict1 = {'anime':'conan',
    'song':'Natural',}

    #antonym
    dict2 = {'anime':'tower of god',
    'food':'pizza',
   }
    expected=[['anime', 'conan', 'tower of god'], ['song', 'Natural', None]]
    actual= left_join(dict1,dict2)
    assert expected==actual

def test_3():
    dict1 = {'anime':'The Rising of the Shield Hero',
    'song':'bad liar',}

    dict2 = {
    'food':'pizza',
   }
    expected=[['anime', 'The Rising of the Shield Hero', None], ['song', 'bad liar', None]]
    actual= left_join(dict1,dict2)
    assert expected==actual


def test_4():
    dict1 = {}

    dict2 = {
    'food':'pizza',
   }
    expected=[]
    actual= left_join(dict1,dict2)
    assert expected==actual
