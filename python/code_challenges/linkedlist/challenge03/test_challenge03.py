# Write your test here
import pytest
from challenge03 import linkedList

def testA():
    llist = linkedList()
    llist.append(5)
    llist.append(4)
    llist.append(3)
    llist.append(2)
    llist.append(1)
    llist.deleteNTHNode(2)
    actual =llist.printAll()
    expected = [1, 2, 3 ,5]
    assert actual == expected

def test1():
    llist = linkedList()
    llist.append(1)
    llist.deleteNTHNode(1)
    actual =llist.printAll()
    expected = []
    assert actual == expected

def test2():
    llist = linkedList()
    llist.append(2)
    llist.append(1)
    llist.deleteNTHNode(1)
    actual =llist.printAll()
    expected = [1]
    assert actual == expected