# Write your test here

import pytest
from challenge01 import MyQueue

def testPush():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    expected = 1
    actual = queue.peek()
    assert actual == expected

def testPop():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    expected = 1
    actual = queue.pop()
    assert actual == expected

def testEmpty():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    expected = False
    actual = queue.empty()
    assert actual == expected

def testEmpty2():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.pop()
    queue.pop()
    expected = True
    actual = queue.empty()
    assert actual == expected