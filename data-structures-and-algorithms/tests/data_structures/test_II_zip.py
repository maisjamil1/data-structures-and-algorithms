from data_structures_and_algorithms.data_structures.LinkedList.LinkedList import LinkedList
from data_structures_and_algorithms.data_structures.II_zip.II_zip import zipLists


def test_zipLists1():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert zipLists(llist1,llist2).__str__() =="<3 -><8 -><2 -><7 -><1 -><6 ->None"
# ________________________________________________________________
def test_zipLists2():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
    llist1.append(0) 
    llist1.append(0) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert zipLists(llist1,llist2).__str__() =="<3 -><8 -><2 -><7 -><1 -><6 -><0 -><0 ->None"
# ________________________________________________________________
def test_zipLists3():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 

  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    llist2.append(5) 
    llist2.append(5)
    assert zipLists(llist1,llist2).__str__() =="<3 -><8 -><2 -><7 -><1 -><6 -><5 -><5 ->None"
# ________________________________________________________________
def test_zipLists4():
    llist = LinkedList() 
    llist1 = LinkedList([0,0,0]) 
    llist2 = LinkedList([1,2,3]) 
    assert zipLists(llist1,llist2).__str__() =="<0 -><1 -><0 -><2 -><0 -><3 ->None"