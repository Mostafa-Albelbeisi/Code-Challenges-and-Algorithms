# Write your test here

# Write your test here
import pytest
from challenge02 import validParentheses

def test():
    actual = validParentheses('()')
    expected = True
    assert actual == expected

def test2():
    actual = validParentheses('()[]{}')
    expected = True
    assert actual == expected

def test3():
    actual = validParentheses('[({}]')
    expected = False
    assert actual == expected

def test4():
    actual = validParentheses('[(hello)()]')
    expected = True
    assert actual == expected

def test5():
    actual = validParentheses('[{(())}]')
    expected = True
    assert actual == expected
