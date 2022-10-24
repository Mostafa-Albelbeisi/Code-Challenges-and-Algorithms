# Write your test here
import pytest
from challenge02 import linkedlist, findMidNode

def test_middle():
    actual = findMidNode([1,2,3,4,5])  
    expected = 3
    assert actual == expected

def test_middle1():
    actual = findMidNode([1,2,3,4,5,6])  
    expected = 4
    assert actual == expected

def test_middle2():
    actual = findMidNode(['A','B','C','D','E','F','G'])  
    expected = 'D'
    assert actual == expected

def test_middle3():
    actual = findMidNode(['A','B','C','D','E','F','G','H'])  
    expected = 'E'
    assert actual == expected
        