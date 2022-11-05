# Write your test here
import pytest
from challenge01 import *


@pytest.fixture
def prepared_tree():
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)
    return tree


#////////////////////////////////////preorder/////////////////////////////////////////////


def test_pre_order(prepared_tree):
    assert prepared_tree.preorder() == [3, 9, 20, 15, 7]


def test_pre_order_empty_tree():
    tree = BinaryTree()
    assert tree.preorder() == []

#////////////////////////////////////inorder/////////////////////////////////////////////

def test_in_order(prepared_tree):
    assert prepared_tree.inorder() == [9, 3, 15, 20, 7]

def test_in_order_empty_tree():
    tree = BinaryTree()
    assert tree.inorder() == []



#////////////////////////////////////Tree is empty/////////////////////////////////////////////
def test_tree_empty():
    tree = BinaryTree()
    assert tree.preorder() ==[]
    assert tree.inorder() ==[]


#///////////////////////////////////////////////traversal//////////////////////////////////
    breadth=BinaryTree()
    breadth.root = Node(3)
    breadth.root.left = Node(9)
    breadth.root.right = Node(20)
    breadth.root.left.left = Node(15)
    breadth.root.right.left = Node(7)
    assert breadth.traversal()==[3, 9, 20, 15, 7]