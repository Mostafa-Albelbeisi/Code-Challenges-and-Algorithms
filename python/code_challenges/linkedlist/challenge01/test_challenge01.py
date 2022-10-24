# Write your test here
import pytest 
from challenge01 import Node , linkedlist, deleteNode

linkedList1 = linkedlist()
node1 = Node("1")
linkedList1.append(node1)

node2 = Node("2")
linkedList1.append(node2)

node3 = Node("3")
linkedList1.append(node3)

node4 = Node("4")
linkedList1.append(node4)

node5 = Node("5")
linkedList1.append(node5)


def test_append():
    
    actual=linkedList1.test_fun()
    expected=["1","2","3","4","5"]
    assert actual==expected

def test_delete1():
    
    deleteNode(node1)

    actual=linkedList1.test_fun()
    expected=["2","3","4","5"]
    assert actual==expected

def test_delete2():
    
    deleteNode(node3)

    actual=linkedList1.test_fun()
    expected=["2","4","5"]
    assert actual==expected








    
    