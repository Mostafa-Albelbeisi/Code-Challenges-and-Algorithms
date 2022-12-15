# Write your test here
from challenge02 import repeatedWord
import pytest

def test1():
    expected = "ASAC"
    actual = repeatedWord("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
    assert actual == expected

def test2():
    expected = "No Repetition"
    actual = repeatedWord("I am learning programming at ASAC.")
    assert actual == expected