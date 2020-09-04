from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import Queue,AnimalShelter,Dog,Cat
import pytest

def test_Happy_path_cats_enqueue():
        animals_Shelter=AnimalShelter()
        animals_Shelter.enqueue('first cat','cat')
        animals_Shelter.enqueue('second cat','cat')       
        assert animals_Shelter.cats_queue.__str__()=='<first cat -><second cat ->None'



def test_Happy_path_dogs_enqueue():
        animals_Shelter=AnimalShelter()
        animals_Shelter.enqueue('first dog','dog')
        animals_Shelter.enqueue('second dog','dog')
        assert animals_Shelter.dogs_queue.__str__()=='<first dog -><second dog ->None'


def test_Happy_path_dogs_dequeue():
        animals_Shelter=AnimalShelter()
        animals_Shelter.enqueue('first dog','dog')
        animals_Shelter.enqueue('second dog','dog')
        assert animals_Shelter.dequeue('dog')=='first dog'


def test_Happy_path_cats_dequeue():
        animals_Shelter=AnimalShelter()
        animals_Shelter.enqueue('first cat','cat')
        animals_Shelter.enqueue('second cat','cat')
        assert animals_Shelter.dequeue('cat')=='first cat'


def test_fail_capital_letter_dequeue():
        animals_Shelter=AnimalShelter()
        animals_Shelter.enqueue('first cat','CAT')
        animals_Shelter.enqueue('second cat','CAT')
        assert animals_Shelter.dequeue('CAT')=='first cat'



def test_fail_capital_letter_dequeue():
        animals_Shelter=AnimalShelter()
        animals_Shelter.enqueue('first dog','DOG')
        animals_Shelter.enqueue('second dog','DOG')
        assert animals_Shelter.dequeue('DOG')=='first dog'


def test_edge_case_new_type():
        animals_Shelter=AnimalShelter()
        animals_Shelter.enqueue('first dog','DOG')
        animals_Shelter.enqueue('first cat','CAT')
        assert animals_Shelter.dequeue('snake')==None